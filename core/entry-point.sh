#!/bin/bash


# Colors
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
CYAN="\033[0;36m"
NC="\033[0m" # No Color

SCRIPT_DIR=$(dirname "$(realpath "$0")")
cd "$SCRIPT_DIR" || exit
pwd

echo -e  "${CYAN}==> Checking .env ${NC}"
if [ ! -d "../../.env" ]; then
  echo -e  "${RED}==> .env file not found!${NC}"
  echo -e "${YELLOW}==> Creating .env file...${NC}"
  python3 -m venv ../../.env
  source .env/bin/activate
fi
source .env/bin/activate

echo -e "${CYAN}==> Updating dependencies${NC}"
pip install -r ../requirements.txt 


# create tables
echo -e "${CYAN}==> Updating Database Tables${NC}"
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py spectacular --file schema.yml
echo -e  "${GREEN}==> The Database has been updated${NC}"

echo -e "${YELLOW}==> Creating superuser...${NC}"
# if [ "$CONTAINER_NAME" = "django-app" ]; then
cat create_superuser.py | python3 manage.py shell
# fi
echo -e "${GREEN}==> Starting the Server${NC}"
python3 manage.py runserver

