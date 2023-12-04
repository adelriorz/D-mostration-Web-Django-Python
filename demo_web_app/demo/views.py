from django.shortcuts import render
from .forms import DataPointForm
from .models import DataPoint
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def line_chart(request):
    form = DataPointForm(request.GET or None)

    if form.is_valid():
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        
        # Query the database for data points within the selected date range
        data_points = DataPoint.objects.filter(date__range=(start_date, end_date))
        
        # Create a line chart
        plt.plot(data_points.values_list('date', flat=True), data_points.values_list('value', flat=True))
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.title('Line Chart of Data Points')
        
        # Format the x-axis dates
        plt.gca().xaxis.set_major_locator(plt.MaxNLocator(prune='both'))
        
        # Save the plot to a BytesIO buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()

        # Convert the plot to base64 for embedding in HTML
        chart_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
    else:
        chart_image = None

    return render(request, 'core/line_chart.html', {'form': form, 'chart_image': chart_image})
