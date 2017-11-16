import webbrowser
import sublime, sublime_plugin

class CheckBlDomain(sublime_plugin.TextCommand):
	
	def run(self, edit, url):

		selection = ""
		for region in self.view.sel():
			selection += self.view.substr(region)

		selection = selection.replace('_','-')

		webbrowser.open(url % selection)

		

		
