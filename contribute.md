---
layout: default
title: Contribute
nav_order: 2
has_children: true
has_toc: false
---

# Submit your Questions
Do you have some nice questions to share with the community? Fill in the form below, and you will head over to GitHub (you'll need a GitHub account) to submit your question.
If you have a bigger set of questions to provide you can also reach out directly via [email](mailto:scrumkata@gmail.com) and we can add them.

## Important
Please only submit questions that can be shared publically. If they are copyrighted (maybe they are part of a training) we cannot use them here.
If you have the copyright on the questions you can also let us know and we could add some statements and/or links together with your questions.

**If you submit your question you agree to our [Terms & Conditions](/scrum-kata/terms_conditions/)**

{% include contact-form.html %}


### Thank you to the contributors of Scrum Kata!

<ul class="list-style-none">
{% for contributor in site.github.contributors %}
  <li class="d-inline-block mr-1">
     <a href="{{ contributor.html_url }}"><img src="{{ contributor.avatar_url }}" width="32" height="32" alt="{{ contributor.login }}"/></a>
  </li>
{% endfor %}
</ul>