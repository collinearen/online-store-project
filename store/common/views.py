class TitleMixin:
    name_store = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['name_store'] = self.name_store
        return context
