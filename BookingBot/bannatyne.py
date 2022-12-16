from selenium import webdriver
from html import escape

# Set up the webdriver
driver = webdriver.Firefox()
driver.get("https://bannatyne-services.brightlime.com/memberservice/booking/")

# Find the h3 elements
h3_elements = driver.find_elements_by_css_selector("h3 span.wed")

# Create the table HTML
table_html = "<table>"
table_html += "<tr><th>h3 class</th><th>span class</th><th>h3 id</th></tr>"
for _ in range(len(h3_elements)):
    table_html += "<tr></tr>"
table_html += "</table>"

# Insert the attribute values into the table
for i, h3_element in enumerate(h3_elements):
    h3_class = escape(h3_element.get_attribute("class"))
    span_class = escape(h3_element.find_element_by_css_selector("span.wed").get_attribute("class"))
    h3_id = escape(h3_element.get_attribute("id"))
    table_html = table_html[:table_html.index("<tr>", i + 1)] + f"<td>{h3_class}</td><td>{span_class}</td><td>{h3_id}</td>" + table_html[table_html.index("</tr>", i + 1):]

# Insert the table into the page
driver.execute_script(f"document.getElementById('table-container').innerHTML = '{table_html}';")

# Close the webdriver
driver.close()
