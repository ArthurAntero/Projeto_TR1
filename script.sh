#!/bin/bash

# Terminal 1
gnome-terminal --title="Servidor" -- bash -c "python3 simulador.py; exec bash"

sleep 1

# Terminal 2
gnome-terminal --title="Usuário 1" -- bash -c "python3 interfaceGUI.py; exec bash"

# Terminal 3
gnome-terminal --title="Usuário 2" -- bash -c "python3 interfaceGUI.py; exec bash"