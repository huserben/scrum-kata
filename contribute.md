---
layout: default
title: Contribute
nav_order: 2
has_children: true
has_toc: false
---

# Submit your Questions
Do you have some tricky questions to share with the community? Fill in the form below to contribute! It will appear in the questions library after a quick review. Note that you'll need a GitHub account to submit a question.
If you have a set of questions to provide, you can also reach out directly via [email](mailto:scrumkata@gmail.com), and we can add them in bulk to save you time.

## Before you submit
Please make sure to submit questions that can be shared publically. We cannot use them here if they are copyrighted (e.g., they are part of a training or a certification test). If you are not sure, reach out and we can try figuring it out together.
If you have the copyright on the questions, we could add some statements and/or links together with your questions. Do not hesitate to contact us!

**If you submit your question you agree to our [Terms & Conditions](/scrum-kata/terms_conditions/).**

{% include contact-form.html %}


### Thank you to the contributors of Scrum Kata!

<ul class="list-style-none">
{% for contributor in site.github.contributors %}
  <li class="d-inline-block mr-1">
     <a href="{{ contributor.html_url }}"><img src="{{ contributor.avatar_url }}" width="32" height="32" alt="{{ contributor.login }}"/></a>
  </li>
{% endfor %}
</ul>