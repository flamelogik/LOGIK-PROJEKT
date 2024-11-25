#!/bin/bash

# Filename: create_project_directories-US-EN.sh

# -------------------------------------------------------------------------- #

# Create the project directories

# -------------------------------------------------------------------------- #

# Define a variable called 'separator_hash'
separator_hash=$(printf '# %s #' "$(printf -- '-%.0s' {1..75})")

# -------------------------------------------------------------------------- #

# Function to perform all transformations
function string_clean() {
    local input="$1"
    # Remove new lines and carriage returns
    local result=$(echo "$input" | tr -d '\n\r')
    # Convert all characters to uppercase
    result=$(echo "$result" | tr '[:lower:]' '[:upper:]')
    # Convert any non-alphanumeric characters or whitespaces to underscores
    result=$(echo "$result" | tr -c '[:alnum:]' '_')
    # Convert any whitespaces to underscores
    result=$(echo "$result" | tr ' ' '_')
    # Remove any leading or trailing underscores
    result=$(echo "$result" | sed 's/^_*//;s/_*$//')
    # Recursively replace consecutive underscores with a single underscore
    result=$(echo "$result" | sed 's/__*/_/g')
    while [[ "$result" =~ __ ]]; do
        result=$(echo "$result" | sed 's/__*/_/g')
    done
    echo "$result"
}

# -------------------------------------------------------------------------- #

# Generic function to get and confirm user input
function get_user_input() {
    local prompt_text="$1"      # Text to show in the prompt
    local value_name="$2"       # Name of the value being entered (for display)
    local return_var="$3"       # Name of variable to store the result

    while true; do
        # Prompt user for input
        printf "\n%s\n\n" "$separator_hash"
        read -p "  Enter the $prompt_text: " input_value

        # Transform the input
        input_value=$(string_clean "$input_value")

        # Prompt the user to confirm
        printf "\n  Is this the correct %s? %s\n\n" "$value_name" "$input_value"
        read -p "  [Y (Yes) / N (No) / Q (quit)] [Y]: " confirm
        confirm=${confirm:-Y}

        # Convert confirm to uppercase for case-insensitive comparison
        confirm=${confirm^^}

        case $confirm in
            Y|YES)
                printf "\n  Proceeding with %s: %s\n" "$value_name" "$input_value"
                eval "$return_var='$input_value'"
                return 0
                ;;
            N|NO)
                printf "  Please enter the %s again.\n" "$value_name"
                ;;
            Q|QUIT)
                printf "  Exiting script.\n"
                exit 0
                ;;
            *)
                printf "  Invalid input. Please enter Y, N, or Q.\n"
                ;;
        esac

        printf "\n"
    done
}

# -------------------------------------------------------------------------- #

# Print a message to the user
printf "\n%s\n\n" "$separator_hash"
printf "  Create Project Directories\n"

# Get all required information
get_user_input "Client Name" "client name" "client_name"
get_user_input "Campaign Name" "campaign name" "campaign_name"
get_user_input "Project ID" "project ID" "project_id"

# -------------------------------------------------------------------------- #

# Create concatenated project name
concatenated_project_name="${client_name}_${campaign_name}_${project_id}"

# -------------------------------------------------------------------------- #

# Display final project name
printf "\n%s\n\n" "$separator_hash"
printf "  Final Project Name: %s\n" "$concatenated_project_name"

# -------------------------------------------------------------------------- #

# Define the /mnt/Publicidade/ADV directory
base_directory="/mnt/Publicidade/ADV"

# Echo the base directory
printf "\n%s\n\n" "$separator_hash"
printf "  Base Directory: %s\n" "$base_directory"

# -------------------------------------------------------------------------- #

# prompt user to confirm the creation of the project directories
while true; do
    printf "\n%s\n\n" "$separator_hash"
    printf "  Do you want to create the project directories? \n"
    read -p "  [Y (Yes) / N (No) / Q (quit)] [Y]: " confirm_create
    confirm_create=${confirm_create:-Y}

    # Convert confirm to uppercase for case-insensitive comparison
    confirm_create=${confirm_create^^}

    case $confirm_create in
        Y|YES)
            printf "\n  Creating project directories...\n"
            break
            ;;
        N|NO)
            printf "  Exiting script.\n"
            exit 0
            ;;
        Q|QUIT)
            printf "  Exiting script.\n"
            exit 0
            ;;
        *)
            printf "  Invalid input. Please enter Y, N, or Q.\n"
            ;;
    esac
done

# Create the project directory
project_directory="$base_directory/$concatenated_project_name"
mkdir -p "$project_directory"

# -------------------------------------------------------------------------- #

# Change to the project directory
cd "$project_directory" || exit

# -------------------------------------------------------------------------- #

# Create O2-Pos-SP default project directories
mkdir -p 01_PROJETO/ARTE/{01_AEP,02_PSD,03_C4D,04_AI,05_INDD,06_OUT_COLLECT,_ASSETS/{AUDIO,FONT,MODEL,PRE_RENDER/{AE,C4D},STILL,VIDEO}}
mkdir -p 01_PROJETO/{COR,EDIT/Adobe\ Premiere\ Pro\ Auto-Save,FINALIZADOR}
mkdir -p 03_EDLs_XMLs_AAfs
mkdir -p 04_OFFLINES/{_APROVADOS,DATA}
mkdir -p 05_VFX/3D/{00_IN/sound,01_PLATES/SHOT_NAME,02_TRACKING/SHOT_NAME,03_ASSETS/{ASS,ASSET_NAME/{MODEL,RIGGING,TEXTURE},OBJ_FBX},04_CACHE_RELEASE/{alembic,nCache/fluid,particles,timeEditor},05_SCENES/SHOT_NAME/publish,06_TEXTURES/{3dPaintTextures,fur/{furAttrMap,furEqualMap,furFiles,furImages,furShadowMap}},07_COMP/SHOT_NAME,08_RENDER_OUTPUT,09_PREVIEWS_OUT,10_SHADER,11_MAYA_FILES/{3dPaintTextures,autosave,Clip\ Exports,data/depth,nCache,scripts,sound}}
mkdir -p 05_VFX/ARTE/IN/{FONT,PRJ_EXTERNO/{AEP,AI,C4D,FCP,INDD,PSD,XML},STILL,VIDEO}
mkdir -p 05_VFX/ARTE/OUT
mkdir -p 05_VFX/COMP/{IN,OUT}
mkdir -p 05_VFX/GRADING
mkdir -p 06_REFS
mkdir -p 07_DOCUMENTOS/{APs,CLAQUETES/{FONT,MIDIA},CRONO,FRAMES/{IN,OUT},LISTA_VFX,PLANO_DE_FILMAGEM,PPM,REPORTS/{BOLETINS_CONT,BOLETINS_SOM,LOGGER},ROTEIRO,STORYBOARDS,TRATAMENTO,WORKFLOW}
mkdir -p 09_MASTER/BASE_LIMPA
mkdir -p 10_AUDIO/{_COPIAS,IN,OUT}
mkdir -p 11_CLAQUETES/EXPORT/{IN,OUT}
mkdir -p 11_CLAQUETES/TEMPLATE_NOVA_CLAQUETE/HD
mkdir -p 12_TRABALHO/_APROVADOS
mkdir -p 13_CC/{CHECK,IN,OUT,PROJETO,ROTEIRO,SRT}
mkdir -p 14_DELIVERIES/{APROVACAO,COPIAS/_data/_roteiro/_duracao,ESPECIFICACOES,PEDIDOS/_data/_roteiro/_duracao,PROJETO}
mkdir -p 15_REPERTORIO/{ARTE,COMP,COR}

# # Create directories using curly braces
# mkdir -p 01_PROJETO/ARTE/{ \
#     01_AEP, \
#     02_PSD, \
#     03_C4D, \
#     04_AI, \
#     05_INDD, \
#     06_OUT_COLLECT, \
#     _ASSETS/{ \
#         AUDIO, \
#         FONT, \
#         MODEL, \
#         PRE_RENDER/{ \
#             AE, \
#             C4D \
#         }, \
#         STILL, \
#         VIDEO \
#     } \
# }
# mkdir -p 01_PROJETO/{ \
#     COR, \
#     EDIT/Adobe\ Premiere\ Pro\ Auto-Save, \
#     FINALIZADOR \
# }
# mkdir -p 03_EDLs_XMLs_AAfs
# mkdir -p 04_OFFLINES/{ \
#     _APROVADOS, \
#     DATA \
# }
# mkdir -p 05_VFX/3D/{ \
#     00_IN/sound, \
#     01_PLATES/SHOT_NAME, \
#     02_TRACKING/SHOT_NAME, \
#     03_ASSETS/{ \
#         ASS, \
#         ASSET_NAME/{ \
#             MODEL, \
#             RIGGING, \
#             TEXTURE \
#         }, \
#         OBJ_FBX \
#     }, \
#     04_CACHE_RELEASE/{ \
#         alembic, \
#         nCache/fluid, \
#         particles, \
#         timeEditor \
#     }, \
#     05_SCENES/SHOT_NAME/publish, \
#     06_TEXTURES/{ \
#         3dPaintTextures, \
#         fur/{ \
#             furAttrMap, \
#             furEqualMap, \
#             furFiles, \
#             furImages, \
#             furShadowMap \
#         } \
#     }, \
#     07_COMP/SHOT_NAME, \
#     08_RENDER_OUTPUT, \
#     09_PREVIEWS_OUT, \
#     10_SHADER, \
#     11_MAYA_FILES/{ \
#         3dPaintTextures, \
#         autosave, \
#         Clip\ Exports, \
#         data/depth, \
#         nCache, \
#         scripts, \
#         sound \
#     } \
# }
# mkdir -p 05_VFX/ARTE/IN/{ \
#     FONT, \
#     PRJ_EXTERNO/{ \
#         AEP, \
#         AI, \
#         C4D, \
#         FCP, \
#         INDD, \
#         PSD, \
#         XML \
#     }, \
#     STILL, \
#     VIDEO \
# }
# mkdir -p 05_VFX/ARTE/OUT
# mkdir -p 05_VFX/COMP/{IN,OUT}
# mkdir -p 05_VFX/GRADING
# mkdir -p 06_REFS
# mkdir -p 07_DOCUMENTOS/{ \
#     APs, \
#     CLAQUETES/{ \
#         FONT, \
#         MIDIA \
#     }, \
#     CRONO, \
#     FRAMES/{ \
#         IN, \
#         OUT \
#     }, \
#     LISTA_VFX, \
#     PLANO_DE_FILMAGEM, \
#     PPM, \
#     REPORTS/{ \
#         BOLETINS_CONT, \
#         BOLETINS_SOM, \
#         LOGGER \
#     }, \
#     ROTEIRO, \
#     STORYBOARDS, \
#     TRATAMENTO, \
#     WORKFLOW \
# }
# mkdir -p 09_MASTER/BASE_LIMPA
# mkdir -p 10_AUDIO/{ \
#     _COPIAS, \
#     IN, \
#     OUT \
# }
# mkdir -p 11_CLAQUETES/EXPORT/{ \
#     IN, \
#     OUT \
# }
# mkdir -p 11_CLAQUETES/TEMPLATE_NOVA_CLAQUETE/HD
# mkdir -p 12_TRABALHO/_APROVADOS
# mkdir -p 13_CC/{ \
#     CHECK, \
#     IN, \
#     OUT, \
#     PROJETO, \
#     ROTEIRO, \
#     SRT \
# }
# mkdir -p 14_DELIVERIES/{ \
#     APROVACAO, \
#     COPIAS/_data/_roteiro/_duracao, \
#     ESPECIFICACOES, \
#     PEDIDOS/_data/_roteiro/_duracao, \
#     PROJETO \
# }
# mkdir -p 15_REPERTORIO/{ \
#     ARTE, \
#     COMP, \
#     COR \
# }

# -------------------------------------------------------------------------- #

# Create LOGIK-PROJEKT directories
mkdir -p ativos
mkdir -p backup
mkdir -p cenas
mkdir -p cfg
mkdir -p docs
mkdir -p editorial
mkdir -p flame
mkdir -p mestres
mkdir -p referência
mkdir -p software
mkdir -p tmp
mkdir -p tomadas
mkdir -p trabalho_em_andamento
mkdir -p utilitários
mkdir -p versão

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:

# -------------------------------------------------------------------------- #
