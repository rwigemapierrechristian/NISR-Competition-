# NISR-Competition-
# LABOR FORCE DASHBOARD

This Streamlit application offers a visual representation of labor force statistics for the year 2022. The dashboard comprises various charts and visualizations based on the data imported from the 'RLFS Tables_ Annual_2022.xlsx' Excel file. The application uses Plotly Express for generating charts.

### Data Loading and Processing
The data is loaded from multiple sheets within the Excel file and stored as DataFrames using Pandas. Calculations are performed to derive necessary values for the visualizations.

### Charts and Visualizations
1. **Pie Chart for Labor Force Distribution**: Shows the distribution of males and females in the total inactive population.
2. **Donut Chart for Employment and Unemployment Rates**: Illustrates employment and unemployment rates for males and females.
3. **Bar Chart for Outside Labor Force**: Displays the distribution of males and females outside the labor force.
4. **Line Charts for Population Distribution by Age and Employment Distribution**: Shows population and employment distribution trends across years for males, females, urban, and rural areas.
5. **Area Charts for Population Distribution by Occupation**: Depicts the distribution of males, females, urban, and rural populations across various professions and managerial positions.

### Presentation and Styling
The layout is configured to a wide layout using Streamlit's set_page_config. Custom CSS is used for defining colors and styling. The header includes an image (NISR.png), the main title, and an SVG image (logo.svg).

### Footer
The footer contains an SVG image (logo.svg) and additional information about the competition and a link to the Statistics Rwanda publication.

The code is organized into sections for data processing, chart creation, and layout organization using Streamlit's columns.

For any further information or improvements, refer to the official documentation or comments in the code.
