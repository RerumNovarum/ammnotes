---
layout: page
title: Probability lecture notes
permalink: /pr/
---
{% for p in site.pr %}
### [ {{p.title}} ]( {{p.url}} ) ###
{{ p.content }}
*** 
{% endfor %}
