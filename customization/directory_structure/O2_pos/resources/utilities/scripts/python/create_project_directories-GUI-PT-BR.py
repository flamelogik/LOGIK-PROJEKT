#!/usr/bin/env python3

import os
import re
import sys
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional
import threading

class ProjectDirectoryCreatorGUI:
    def __init__(self):
        self.separator_hash = f"# {'-' * 75} #"
        self.base_directory = "/mnt/Publicidade/ADV"

        # Create main window
        self.root = tk.Tk()
        self.root.title("Criar Diretórios do Projeto")
        self.root.geometry("960x540")

        # Style configuration
        self.style = ttk.Style()
        self.style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        self.style.configure('Info.TLabel', font=('Arial', 10))

        self.creating_directories = False
        self.create_gui()

    def create_gui(self):
        """Create the GUI elements"""
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Title
        title_label = ttk.Label(main_frame, text="Criar Diretórios do Projeto", style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Base directory display
        base_dir_label = ttk.Label(main_frame, text="Diretório Base:", style='Header.TLabel')
        base_dir_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        base_dir_value = ttk.Label(main_frame, text=self.base_directory, style='Info.TLabel')
        base_dir_value.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=(0, 20))

        # Input fields
        input_frame = ttk.LabelFrame(main_frame, text="Informações do Projeto", padding="10")
        input_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))

        # Client Name
        ttk.Label(input_frame, text="Nome do Cliente:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.client_name_var = tk.StringVar()
        self.client_name_entry = ttk.Entry(input_frame, textvariable=self.client_name_var, width=90)
        self.client_name_entry.grid(row=0, column=1, sticky=tk.W, pady=5)

        # Campaign Name
        ttk.Label(input_frame, text="Nome da Campanha:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.campaign_name_var = tk.StringVar()
        self.campaign_name_entry = ttk.Entry(input_frame, textvariable=self.campaign_name_var, width=90)
        self.campaign_name_entry.grid(row=1, column=1, sticky=tk.W, pady=5)

        # Project ID
        ttk.Label(input_frame, text="ID do Projeto:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.project_id_var = tk.StringVar()
        self.project_id_entry = ttk.Entry(input_frame, textvariable=self.project_id_var, width=90)
        self.project_id_entry.grid(row=2, column=1, sticky=tk.W, pady=5)

        # Preview Frame
        preview_frame = ttk.LabelFrame(main_frame, text="Prévia", padding="10")
        preview_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))

        # Preview Label
        self.preview_var = tk.StringVar(value="Nome Final do Projeto: ")
        self.preview_label = ttk.Label(preview_frame, textvariable=self.preview_var, wraplength=720)
        self.preview_label.grid(row=0, column=0, sticky=tk.W)

        # # Progress Frame
        # self.progress_frame = ttk.LabelFrame(main_frame, text="Progress", padding="10")
        # self.progress_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))

        # # Progress Bar
        # self.progress_var = tk.DoubleVar()
        # self.progress_bar = ttk.Progressbar(self.progress_frame, variable=self.progress_var, maximum=90)
        # self.progress_bar.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=5, pady=5)

        # # Progress Label
        # self.progress_label = ttk.Label(self.progress_frame, text="")
        # self.progress_label.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=5, pady=5)

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E))
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)

        # Preview Button
        self.preview_btn = ttk.Button(button_frame, text="Atualizar Prévia", command=self.update_preview)
        self.preview_btn.grid(row=0, column=0, padx=5)

        # Create Button
        self.create_btn = ttk.Button(button_frame, text="Criar Diretórios", command=self.create_directories)
        self.create_btn.grid(row=0, column=1, padx=5)

        # Exit Button
        self.exit_btn = ttk.Button(button_frame, text="Sair", command=self.quit_application)
        self.exit_btn.grid(row=0, column=2, padx=5)

        # Bind events
        self.client_name_var.trace('w', lambda *args: self.update_preview())
        self.campaign_name_var.trace('w', lambda *args: self.update_preview())
        self.project_id_var.trace('w', lambda *args: self.update_preview())

    def string_clean(self, input_str: str) -> str:
        """Clean and format input string according to project naming conventions."""
        result = input_str.strip()
        result = result.upper()
        result = re.sub(r'[^a-zA-Z0-9]', '_', result)
        result = result.strip('_')
        result = re.sub(r'_+', '_', result)
        return result

    def update_preview(self, *args):
        """Update the preview of the project name"""
        client = self.string_clean(self.client_name_var.get())
        campaign = self.string_clean(self.campaign_name_var.get())
        project_id = self.string_clean(self.project_id_var.get())

        if client and campaign and project_id:
            project_name = f"{client}_{campaign}_{project_id}"
            self.preview_var.set(f"Nome Final do Projeto: {project_name}")
        else:
            self.preview_var.set("Nome Final do Projeto: (Preencha todos os campos)")

    def validate_inputs(self) -> bool:
        """Validate all input fields"""
        if not self.client_name_var.get().strip():
            messagebox.showerror("Erro", "Por favor, insira o nome do cliente.")
            return False
        if not self.campaign_name_var.get().strip():
            messagebox.showerror("Erro", "Por favor, insira o nome da campanha.")
            return False
        if not self.project_id_var.get().strip():
            messagebox.showerror("Erro", "Por favor, insira o ID do projeto.")
            return False
        return True

    def create_directories(self):
        """Initiate directory creation process"""
        if self.creating_directories:
            return

        if not self.validate_inputs():
            return

        client = self.string_clean(self.client_name_var.get())
        campaign = self.string_clean(self.campaign_name_var.get())
        project_id = self.string_clean(self.project_id_var.get())
        project_name = f"{client}_{campaign}_{project_id}"

        # Confirm directory creation
        if not messagebox.askyesno("Confirmar",
                                 f"Você quer criar os diretórios do projeto?\n\n"
                                 f"Nome do Projeto: {project_name}\n"
                                 f"Diretório Base: {self.base_directory}"):
            return

        # Disable buttons during creation
        self.creating_directories = True
        self.toggle_buttons()

        # Start directory creation in a separate thread
        thread = threading.Thread(target=self.create_directory_structure,
                                args=(Path(self.base_directory) / project_name,))
        thread.start()

    def create_directory_structure(self, project_path: Path):
        """Create the complete directory structure."""
        try:
            # Update progress bar visibility
            self.root.after(0, lambda: self.progress_label.config(
                text="Iniciando criação dos diretórios..."))

            # Create base project directory
            project_path.mkdir(parents=True, exist_ok=True)

            # Define all directories (same as before)
            directories = [
                # All directories from the previous version...
                # O2-Pos-SP directories
                "01_PROJETO/ARTE/01_AEP",
                "01_PROJETO/ARTE/02_PSD",
                "01_PROJETO/ARTE/03_C4D",
                "01_PROJETO/ARTE/04_AI",
                "01_PROJETO/ARTE/05_INDD",
                "01_PROJETO/ARTE/06_OUT_COLLECT",
                "01_PROJETO/ARTE/_ASSETS/AUDIO",
                "01_PROJETO/ARTE/_ASSETS/FONT",
                "01_PROJETO/ARTE/_ASSETS/MODEL",
                "01_PROJETO/ARTE/_ASSETS/PRE_RENDER/AE",
                "01_PROJETO/ARTE/_ASSETS/PRE_RENDER/C4D",
                "01_PROJETO/ARTE/_ASSETS/STILL",
                "01_PROJETO/ARTE/_ASSETS/VIDEO",
                "01_PROJETO/COR",
                "01_PROJETO/EDIT/Adobe Premiere Pro Auto-Save",
                "01_PROJETO/FINALIZADOR",
                "03_EDLs_XMLs_AAfs",
                "04_OFFLINES/_APROVADOS",
                "04_OFFLINES/DATA",
                # VFX directories
                "05_VFX/3D/00_IN/sound",
                "05_VFX/3D/01_PLATES/SHOT_NAME",
                "05_VFX/3D/02_TRACKING/SHOT_NAME",
                "05_VFX/3D/03_ASSETS/ASS",
                "05_VFX/3D/03_ASSETS/ASSET_NAME/MODEL",
                "05_VFX/3D/03_ASSETS/ASSET_NAME/RIGGING",
                "05_VFX/3D/03_ASSETS/ASSET_NAME/TEXTURE",
                "05_VFX/3D/03_ASSETS/OBJ_FBX",
                "05_VFX/3D/04_CACHE_RELEASE/alembic",
                "05_VFX/3D/04_CACHE_RELEASE/nCache/fluid",
                "05_VFX/3D/04_CACHE_RELEASE/particles",
                "05_VFX/3D/04_CACHE_RELEASE/timeEditor",
                "05_VFX/3D/05_SCENES/SHOT_NAME/publish",
                "05_VFX/3D/06_TEXTURES/3dPaintTextures",
                "05_VFX/3D/06_TEXTURES/fur/furAttrMap",
                "05_VFX/3D/06_TEXTURES/fur/furEqualMap",
                "05_VFX/3D/06_TEXTURES/fur/furFiles",
                "05_VFX/3D/06_TEXTURES/fur/furImages",
                "05_VFX/3D/06_TEXTURES/fur/furShadowMap",
                "05_VFX/3D/07_COMP/SHOT_NAME",
                "05_VFX/3D/08_RENDER_OUTPUT",
                "05_VFX/3D/09_PREVIEWS_OUT",
                "05_VFX/3D/10_SHADER",
                "05_VFX/3D/11_MAYA_FILES/3dPaintTextures",
                "05_VFX/3D/11_MAYA_FILES/autosave",
                "05_VFX/3D/11_MAYA_FILES/Clip Exports",
                "05_VFX/3D/11_MAYA_FILES/data/depth",
                "05_VFX/3D/11_MAYA_FILES/nCache",
                "05_VFX/3D/11_MAYA_FILES/scripts",
                "05_VFX/3D/11_MAYA_FILES/sound",
                # Additional directories
                "05_VFX/ARTE/IN/FONT",
                "05_VFX/ARTE/IN/PRJ_EXTERNO/AEP",
                "05_VFX/ARTE/IN/PRJ_EXTERNO/AI",
                "05_VFX/ARTE/IN/PRJ_EXTERNO/C4D",
                "05_VFX/ARTE/IN/PRJ_EXTERNO/FCP",
                "05_VFX/ARTE/IN/PRJ_EXTERNO/INDD",
                "05_VFX/ARTE/IN/PRJ_EXTERNO/PSD",
                "05_VFX/ARTE/IN/PRJ_EXTERNO/XML",
                "05_VFX/ARTE/IN/STILL",
                "05_VFX/ARTE/IN/VIDEO",
                "05_VFX/ARTE/OUT",
                "05_VFX/COMP/IN",
                "05_VFX/COMP/OUT",
                "05_VFX/GRADING",
                "06_REFS",
                "07_DOCUMENTOS/APs",
                "07_DOCUMENTOS/CLAQUETES/FONT",
                "07_DOCUMENTOS/CLAQUETES/MIDIA",
                "07_DOCUMENTOS/CRONO",
                "07_DOCUMENTOS/FRAMES/IN",
                "07_DOCUMENTOS/FRAMES/OUT",
                "07_DOCUMENTOS/LISTA_VFX",
                "07_DOCUMENTOS/PLANO_DE_FILMAGEM",
                "07_DOCUMENTOS/PPM",
                "07_DOCUMENTOS/REPORTS/BOLETINS_CONT",
                "07_DOCUMENTOS/REPORTS/BOLETINS_SOM",
                "07_DOCUMENTOS/REPORTS/LOGGER",
                "07_DOCUMENTOS/ROTEIRO",
                "07_DOCUMENTOS/STORYBOARDS",
                "07_DOCUMENTOS/TRATAMENTO",
                "07_DOCUMENTOS/WORKFLOW",
                "09_MASTER/BASE_LIMPA",
                "10_AUDIO/_COPIAS",
                "10_AUDIO/IN",
                "10_AUDIO/OUT",
                "11_CLAQUETES/EXPORT/IN",
                "11_CLAQUETES/EXPORT/OUT",
                "11_CLAQUETES/TEMPLATE_NOVA_CLAQUETE/HD",
                "12_TRABALHO/_APROVADOS",
                "13_CC/CHECK",
                "13_CC/IN",
                "13_CC/OUT",
                "13_CC/PROJETO",
                "13_CC/ROTEIRO",
                "13_CC/SRT",
                "14_DELIVERIES/APROVACAO",
                "14_DELIVERIES/COPIAS/_data/_roteiro/_duracao",
                "14_DELIVERIES/ESPECIFICACOES",
                "14_DELIVERIES/PEDIDOS/_data/_roteiro/_duracao",
                "14_DELIVERIES/PROJETO",
                "15_REPERTORIO/ARTE",
                "15_REPERTORIO/COMP",
                "15_REPERTORIO/COR",
                # LOGIK-PROJEKT directories
                "ativos",
                "backup",
                "cenas",
                "cfg",
                "docs",
                "editorial",
                "flame",
                "mestres",
                "referência",
                "software",
                "tmp",
                "tomadas",
                "trabalho_em_andamento",
                "utilitários",
                "versão"
            ]


            total_dirs = len(directories)
            for idx, directory in enumerate(directories, 1):
                if not self.creating_directories:  # Check if cancelled
                    break

                full_path = project_path / directory
                full_path.mkdir(parents=True, exist_ok=True)

                # Update progress
                progress = (idx / total_dirs) * 100
                self.root.after(0, lambda p=progress: self.progress_var.set(p))
                self.root.after(0, lambda d=directory: self.progress_label.config(
                    text=f"Criando: {d}"))

            if self.creating_directories:  # Only show success if not cancelled
                self.root.after(0, lambda: messagebox.showinfo("Sucesso",
                    "Diretórios do projeto foram criados com sucesso!"))

        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Erro",
                f"Erro ao criar diretórios:\n{str(e)}"))

        finally:
            self.creating_directories = False
            self.root.after(0, self.toggle_buttons)
            self.root.after(0, lambda: self.progress_var.set(0))
            self.root.after(0, lambda: self.progress_label.config(text=""))

    def toggle_buttons(self):
        """Toggle button states based on directory creation status"""
        state = 'disabled' if self.creating_directories else 'normal'
        self.preview_btn.config(state=state)
        self.create_btn.config(state=state)
        self.exit_btn.config(state=state)
        self.client_name_entry.config(state=state)
        self.campaign_name_entry.config(state=state)
        self.project_id_entry.config(state=state)

    def quit_application(self):
        """Safely quit the application"""
        if self.creating_directories:
            if messagebox.askyesno("Confirmar",
                "Criação de diretórios em andamento. Deseja realmente sair?"):
                self.creating_directories = False
            else:
                return
        self.root.quit()

    def run(self):
        """Start the GUI application"""
        self.root.protocol("WM_DELETE_WINDOW", self.quit_application)
        self.root.mainloop()

if __name__ == "__main__":
    app = ProjectDirectoryCreatorGUI()
    app.run()