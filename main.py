from kivy.app import  App
from kivymd.app import MDApp
from kivy.lang import builder
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.list import MDList
from kivymd.uix.list import OneLineListItem
from kivymd.theming import ThemableBehavior
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDIcon
from kivymd.uix.label import MDLabel
from kivy.utils import platform
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.image import Image

from jnius import autoclass

PythonActivity = autoclass('org.kivy.android.PythonActivity')
Intent = autoclass('android.content.Intent')
Uri = autoclass('android.net.Uri')

class ContentNavigationDrawer(BoxLayout):
    pass

class AboutScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class GemScreen(Screen):
    pass

class Consult(Screen):
    pass



class MainWidget(BoxLayout):
    pass

class MaheshApp(MDApp):

    def build(self):

        return MainWidget()

    def go_to_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name

    def on_start(self):
        pass
        # self.root.transition = SlideTransition()

    def send_message(self, *args):
        phone_number = '8275280055' # replace with the phone number you want to send the message to
        uri = Uri.parse("https://api.whatsapp.com/send?phone=" + phone_number)

        # Create the intent
        intent = Intent(Intent.ACTION_VIEW, uri)

        # Start the activity
        current_activity = PythonActivity.mActivity
        current_activity.startActivity(intent)

    # def send_whatsapp_message(self):
    #     phone_number = '8275280055'
    #     # Retrieve the Java classes needed for the Intent
    #     # PythonActivity = autoclass('org.kivy.android.PythonActivity')
    #     # Intent = autoclass('android.content.Intent')
    #     # Uri = autoclass('android.net.Uri')
    #
    #     # Define the phone number and message body
    #     phone_uri = Uri.parse("smsto:" + phone_number)
    #     intent = Intent(Intent.ACTION_SENDTO, phone_uri)
    #     intent.setPackage("com.whatsapp")
    #     intent.putExtra(Intent.EXTRA_TEXT, "Hi Astro Mahesh")
    #
    #     # Start the WhatsApp activity
    #     current_activity = PythonActivity.mActivity
    #     current_activity.startActivity(intent)


if __name__ == "__main__":
    MaheshApp().run()