import sort_module

import importlib
importlib.reload(sort_module)

choice = ""
path_to_folder = "None"
state_report = "activated"
valid_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]



while choice != "9":

      choice = sort_module.choice_menu(choice, path_to_folder, state_report)

      if choice not in valid_choices:
            sort_module.invalid_input()
      elif choice == "1":
            path_to_folder = sort_module.add_folder_to_sort(path_to_folder)
      elif choice == "2":
            state_report = sort_module.report_on_off(state_report)
      elif choice == "3":
            sort_module.display_sort_list()
      elif choice == "4":
            sort_module.add_extension()
      elif choice == "5":
            sort_module.remove_extension()
      elif choice == "6":
            sort_module.change_dest_folder()
      elif choice == "7":
            sort_module.apply_sort(path_to_folder, state_report)
      elif choice == "8":
            sort_module.display_infos()
      elif choice == "9":
            pass
