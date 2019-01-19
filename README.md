# django-redirect-to-non-www

Redirects ww<span></span>w. URL address to non-ww<span></span>w.

## Installation

```bash
pip install django-redirect-to-non-www
```

```bash
pip install git+https://git@github.com/lukasvinclav/django-redirect-to-non-www.git
```

## Configuration

Open your settings file and append middleware **redirect_to_non_ww<span></span>w.middleware.RedirectToNonWw<span></span>w** at the end of **MIDDLEWARE** list.

```python
MIDDLEWARE = [
    # Other middleware classes
    'redirect_to_non_www.middleware.RedirectToNonWww',
]
```