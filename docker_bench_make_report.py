import json

def generate_html_report(json_data, output_file):
    # Define HTML styles
    html_styles = """
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f4f4;
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            background-color: #fff;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        .title {
            background-color: #007BFF;
            color: white;
            font-weight: bold;
        }
        .info {
            background-color: #F0FFFF;
        }
        .warn {
            background-color: #f2dede;
        }
        .note {
            background-color: #fcf8e3;
        }
        .pass {
            background-color: #dff0d8;
        }
    </style>
    """
    
    # Start HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Docker Bench Report</title>
        {styles}
    </head>
    <body>
        <h1>Docker Bench Report</h1>
        <table>
            <thead>
                <tr>
                    <th>Tag</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
    """.format(styles=html_styles)
    
    # Add rows to HTML content
    for item in json_data:
        row_class = ''
        if item['title']:
            row_class = 'title'
        elif item['tag'] == '[INFO]':
            row_class = 'info'
        elif item['tag'] == '[WARN]':
            row_class = 'warn'
        elif item['tag'] == '[NOTE]':
            row_class = 'note'
        elif item['tag'] == '[PASS]':
            row_class = 'pass'
        
        html_content += """
            <tr class="{row_class}">
                <td>{tag}</td>
                <td>{description}</td>
            </tr>
        """.format(row_class=row_class, tag=item['tag'], description=item['description'])
    
    # Close HTML content
    html_content += """
            </tbody>
        </table>
    </body>
    </html>
    """
    
    # Write HTML content to file
    with open(output_file, 'w') as file:
        file.write(html_content)
    print(f"Report has been written to {output_file}")

def main():
    # Path to the input JSON file
    input_json_file = 'json_output\\docker_bench_results.json'
    
    # Path to the output HTML file
    output_html_file = 'docker_bench_report.html'
    
    # Read JSON data from file
    with open(input_json_file, 'r') as file:
        json_data = json.load(file)
    
    # Generate HTML report
    generate_html_report(json_data, output_html_file)

if __name__ == '__main__':
    main()
