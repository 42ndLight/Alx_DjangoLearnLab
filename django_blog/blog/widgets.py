from django.forms import TextInput

class TagWidget(TextInput):
    class Media:
        css = {
            'all': ('css/tag-widget.css',)  # Custom CSS for the widget
        }
        js = ('js/tag-widget.js',)  # Custom JavaScript for the widget

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs.update({'class': 'tag-widget'})  # Add a CSS class for styling
