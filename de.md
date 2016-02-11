---
layout: page
title: Differential equations lecture notes
permalink: /de/
---
{% for p in site.de %}
### [ {{p.title}} ]( {{p.url}} ) ###
{{ p.content }}
*** 
{% endfor %}
