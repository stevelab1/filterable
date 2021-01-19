# filterable

Basic implementation of django-filter

---

Made an adjustment to django_filters/filters.py:

On line 124, changed `self.label` from `value` to `""`

`def fset(self, value):`

`self._label = ""`