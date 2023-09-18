html_code = """
<div class="list-item">
  <a class="item-link" href="/donate/request/{{ request.id }}/">
    <div class="AvatarCardContainer">
      <div class="AvatarFrame">
        <img src="static/images/OIP.jpeg" alt="{{ request.patient_name }}">
      </div>
      <div class="BloodgroupLabel">
        <div class="BloodgroupText">{{ request.blood_group }}</div>
      </div>
      <div class="AvatarLabel">
        <div class="AvatarLabelText">{{ request.patient_name }}</div>
      </div>
    </div>
  </a>
</div>
"""

# Repeat the HTML code 300 times
html_code_repeated = html_code * 300

# Print or use the generated HTML code as needed
print(html_code_repeated)
