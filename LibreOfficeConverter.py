# Nautilus Extension to Convert Documents using LibreOffice
#
# Author: Gemini
# Based on the user's request for multi-format conversion.
#
# To install, place this file in:
# ~/.local/share/nautilus-python/extensions/
#
# Then, restart Nautilus:
# nautilus -q

import os
import subprocess
from gi.repository import Nautilus, GObject
from functools import partial

# Defines the target formats available for each category of document.
CONVERSION_MAP = {
    'word': {
        'targets': {
            'pdf': 'para PDF',
            'docx': 'para Word (.docx)',
            'odt': 'para LibreOffice (.odt)',
            'txt': 'para Texto (.txt)',
        }
    },
    'spreadsheet': {
        'targets': {
            'pdf': 'para PDF',
            'xlsx': 'para Excel (.xlsx)',
            'ods': 'para LibreOffice (.ods)',
            'csv': 'para CSV',
        }
    },
    'presentation': {
        'targets': {
            'pdf': 'para PDF',
            'pptx': 'para PowerPoint (.pptx)',
            'odp': 'para LibreOffice (.odp)',
        }
    }
}

# Groups MIME types into categories.
MIME_TYPE_GROUPS = {
    "application/msword": "word",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "word",
    "application/vnd.oasis.opendocument.text": "word",
    "text/plain": "word",
    "text/rtf": "word",

    "application/vnd.ms-excel": "spreadsheet",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "spreadsheet",
    "application/vnd.oasis.opendocument.spreadsheet": "spreadsheet",

    "application/vnd.ms-powerpoint": "presentation",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": "presentation",
    "application/vnd.oasis.opendocument.presentation": "presentation",
}


class LibreOfficeConverterExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass

    def get_file_items(self, files):
        """
        Adds a submenu to the context menu for supported document files.
        """
        if not files:
            return

        # Determine the category from the first file's MIME type.
        file_category = self._get_file_category(files[0])
        if not file_category:
            return

        # Ensure all selected files belong to the same category.
        if not all(self._get_file_category(f) == file_category for f in files):
            return

        # Create the main menu item and the submenu.
        main_item = Nautilus.MenuItem(
            name="LibreOfficeConverter::Convert",
            label="Converter com LibreOffice",
            tip="Converte o(s) arquivo(s) para outros formatos",
        )
        submenu = Nautilus.Menu()
        main_item.set_submenu(submenu)

        # Populate the submenu with target formats for the file category.
        targets = CONVERSION_MAP[file_category]['targets']
        for format_ext, label in targets.items():
            item = Nautilus.MenuItem(
                name=f"LibreOfficeConverter::ConvertTo{format_ext.upper()}",
                label=label,
                tip=f"Converte para o formato {format_ext.upper()}",
            )
            # Pass the target format to the handler
            item.connect("activate", self._convert_files, files, format_ext)
            submenu.append_item(item)

        return [main_item]

    def _get_file_category(self, file):
        """

        Checks if a file is supported and returns its category ('word', 'spreadsheet', etc.).
        """
        if file.is_directory():
            return None
        return MIME_TYPE_GROUPS.get(file.get_mime_type())

    def _convert_files(self, menu, files, target_format):
        """
        Handles the conversion process for the given files to the target format.
        """
        for file in files:
            filepath = file.get_location().get_path()
            output_dir = os.path.dirname(filepath)

            try:
                command = [
                    "libreoffice",
                    "--headless",
                    "--convert-to",
                    target_format,
                    filepath,
                    "--outdir",
                    output_dir,
                ]
                subprocess.run(command, check=True, capture_output=True, text=True)

            except FileNotFoundError:
                self._show_error_dialog("Comando 'libreoffice' não encontrado. Verifique se o LibreOffice está instalado e no PATH do sistema.")
                return
            except subprocess.CalledProcessError as e:
                error_message = f"Erro ao converter '{os.path.basename(filepath)}'.\n\nErro:\n{e.stderr}"
                self._show_error_dialog(error_message)
            except Exception as e:
                self._show_error_dialog(f"Ocorreu um erro inesperado: {e}")

    def _show_error_dialog(self, message):
        """
        Displays an error message to the user using zenity or kdialog.
        """
        tool = "zenity" if self._is_tool("zenity") else "kdialog" if self._is_tool("kdialog") else None
        if tool:
            subprocess.run([tool, "--error", message, "--title=Erro de Conversão"])
        else:
            print(f"Error: {message}")
            print("Please install 'zenity' or 'kdialog' to see error dialogs.")

    def _is_tool(self, name):
        """Check whether `name` is on PATH and marked as executable."""
        from shutil import which
        return which(name) is not None
