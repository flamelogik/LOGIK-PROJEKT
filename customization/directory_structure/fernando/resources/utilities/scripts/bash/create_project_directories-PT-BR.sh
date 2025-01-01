#!/bin/bash

# Filename: create_project_directories-PT-BR.sh

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
        read -p "  Digite o $prompt_text:  " input_value

        # Transform the input
        input_value=$(string_clean "$input_value")

        # Prompt the user to confirm
        printf "\n  Este é o $value_name correto %s? %s\n\n" "$value_name" "$input_value"
        read -p "  [S (Sim) / N (Não) / Q (Sair)] [S]:  " confirm
        confirm=${confirm:-S}

        # Convert confirm to uppercase for case-insensitive comparison
        confirm=${confirm^^}

        case $confirm in
            S|SIM)
                printf "\n  Prosseguindo com %s: %s\n" "$value_name" "$input_value"
                eval "$return_var='$input_value'"
                return 0
                ;;
            N|NÃO|NAO)
                printf "  Por favor, digite o %s novamente.\n" "$value_name"
                ;;
            Q|SAIR)
                printf "  Saindo do script.\n"
                exit 0
                ;;
            *)
                printf "  Entrada inválida. Por favor, digite S, N, ou Q.\n"
                ;;
        esac

        printf "\n"
    done
}

# -------------------------------------------------------------------------- #

# Print a message to the user
printf "\n%s\n\n" "$separator_hash\n"
printf "  Criar Diretórios do Projeto\n"

# Get all required information
get_user_input "nome do cliente" "nome do cliente" "client_name"
get_user_input "nome da campanha" "nome da campanha" "campaign_name"
get_user_input "ID do projeto" "ID do projeto" "project_id"

# -------------------------------------------------------------------------- #

# Create concatenated project name
concatenated_project_name="${client_name}_${campaign_name}_${project_id}"

# -------------------------------------------------------------------------- #

# Display final project name
printf "\n%s\n\n" "$separator_hash"
printf "  Nome Final do Projeto: %s\n" "$concatenated_project_name"

# -------------------------------------------------------------------------- #

# Define the base directory
# base_directory="/PROJEKTS"
base_directory="/var/tmp/PROJEKTS"

# Echo the base directory
printf "\n%s\n\n" "$separator_hash"
printf "  Diretório Base: %s\n" "$base_directory"

# -------------------------------------------------------------------------- #

# prompt user to confirm the creation of the project directories
while true; do
    printf "\n%s\n\n" "$separator_hash"
    printf "  Você quer criar os diretórios do projeto? "
    read -p "  [S (Sim) / N (Não) / Q (Sair)] [S]: " confirm_create
    confirm_create=${confirm_create:-S}

    # Convert confirm to uppercase for case-insensitive comparison
    confirm_create=${confirm_create^^}

    case $confirm_create in
        S|SIM)
            printf "\n  Criando diretórios do projeto...\n"
            break
            ;;
        N|NÃO|NAO)
            printf "  Saindo do script.\n"
            exit 0
            ;;
        Q|SAIR)
            printf "  Saindo do script.\n"
            exit 0
            ;;
        *)
            printf "  Entrada inválida. Por favor, digite S, N, ou Q.\n"
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

# Create LOGIK-PROJEKT directories
mkdir -p ativos
mkdir -p ativos/arte
mkdir -p ativos/áudio
mkdir -p ativos/diversos
mkdir -p ativos/filmagem
mkdir -p ativos/filmagem_graduada
mkdir -p ativos/gráficos
mkdir -p ativos/gráficos/claquetes
mkdir -p ativos/gráficos/legal
mkdir -p ativos/gráficos/legendas
mkdir -p ativos/gráficos/supers
mkdir -p ativos/gráficos/títulos
mkdir -p ativos/imagens
mkdir -p ativos/matchmove
mkdir -p ativos/pintura
mkdir -p ativos/rotoscopia
mkdir -p backup
mkdir -p cenas
mkdir -p cfg
mkdir -p docs
mkdir -p editorial
mkdir -p editorial/aaf
mkdir -p editorial/edl
mkdir -p editorial/prep
mkdir -p editorial/ref
mkdir -p editorial/xml
mkdir -p flame
mkdir -p flame/arquivos
mkdir -p flame/configurações
mkdir -p mestres
mkdir -p mestres/edições_mestre
mkdir -p mestres/mestres_agendados
mkdir -p mestres/mestres_versionados
mkdir -p referência
mkdir -p referência/filmes_de_referência
mkdir -p referência/guia_de_estilo_de_referência
mkdir -p referência/imagens_de_referência
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
