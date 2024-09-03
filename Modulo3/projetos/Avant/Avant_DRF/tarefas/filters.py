from dj_rql.filter_cls import AutoRQLFilterClass
from tarefas.models import Tarefas


class TarefaFilterClass(AutoRQLFilterClass):
    MODEL = Tarefas

    FILTERS = [{"filter": "user", "source": "user__username"}]
