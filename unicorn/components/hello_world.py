from django.contrib.auth.models import User
from django_unicorn.components import UnicornView


class HelloWorldView(UnicornView):
    name = "World"
    users = User.objects.all()

    # selected_state = ""

    # def select_state(self, state_name, selected_idx):
    #     print("select_state state_name", state_name)
    #     print("select_state selected_idx", selected_idx)
    #     self.selected_state = state_name
