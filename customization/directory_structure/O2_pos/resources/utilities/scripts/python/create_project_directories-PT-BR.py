#!/usr/bin/env python3

import os
import re
from pathlib import Path
import sys

class ProjectDirectoryCreator:
    def __init__(self):
        self.separator_hash = f"# {'-' * 75} #"
        self.base_directory = "/mnt/Publicidade/ADV"

    def string_clean(self, input_str: str) -> str:
        """Clean and format input string according to project naming conventions."""
        # Remove newlines and carriage returns
        result = input_str.strip()
        # Convert to uppercase
        result = result.upper()
        # Convert non-alphanumeric characters to underscores
        result = re.sub(r'[^a-zA-Z0-9]', '_', result)
        # Remove leading/trailing underscores
        result = result.strip('_')
        # Replace multiple underscores with single underscore
        result = re.sub(r'_+', '_', result)
        return result

    def get_user_input(self, prompt_text: str, value_name: str) -> str:
        """Get and confirm user input with validation."""
        while True:
            print(f"\n{self.separator_hash}\n")
            input_value = input(f"  Digite o {prompt_text}:  ")
            input_value = self.string_clean(input_value)

            print(f"\n  Este é o {value_name} correto {value_name}? {input_value}\n")
            confirm = input("  [S (Sim) / N (Não) / Q (Sair)] [S]:  ").upper() or 'S'

            if confirm in ['S', 'SIM']:
                print(f"\n  Prosseguindo com {value_name}: {input_value}")
                return input_value
            elif confirm in ['N', 'NÃO', 'NAO']:
                print(f"  Por favor, digite o {value_name} novamente.")
            elif confirm in ['Q', 'SAIR']:
                print("  Saindo do script.")
                sys.exit(0)
            else:
                print("  Entrada inválida. Por favor, digite S, N, ou Q.")

    def create_directory_structure(self, project_path: Path):
        """Create the complete directory structure."""
        # O2-Pos-SP directories
        directories = [
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

        for directory in directories:
            full_path = project_path / directory
            full_path.mkdir(parents=True, exist_ok=True)
            print(f"  Created: {full_path}")

    def run(self):
        """Main execution flow."""
        print(f"\n{self.separator_hash}\n")
        print("  Criar Diretórios do Projeto\n")

        # Get project information
        client_name = self.get_user_input("nome do cliente", "nome do cliente")
        campaign_name = self.get_user_input("nome da campanha", "nome da campanha")
        project_id = self.get_user_input("ID do projeto", "ID do projeto")

        # Create project name
        project_name = f"{client_name}_{campaign_name}_{project_id}"

        print(f"\n{self.separator_hash}\n")
        print(f"  Nome Final do Projeto: {project_name}")
        print(f"\n{self.separator_hash}\n")
        print(f"  Diretório Base: {self.base_directory}")

        # Confirm directory creation
        while True:
            print(f"\n{self.separator_hash}\n")
            confirm = input("  Você quer criar os diretórios do projeto? [S (Sim) / N (Não) / Q (Sair)] [S]: ").upper() or 'S'

            if confirm in ['S', 'SIM']:
                print("\n  Criando diretórios do projeto...")
                break
            elif confirm in ['N', 'NÃO', 'NAO', 'Q', 'SAIR']:
                print("  Saindo do script.")
                sys.exit(0)
            else:
                print("  Entrada inválida. Por favor, digite S, N, ou Q.")

        # Create project directory
        project_path = Path(self.base_directory) / project_name
        self.create_directory_structure(project_path)

if __name__ == "__main__":
    creator = ProjectDirectoryCreator()
    creator.run()