Steps to follow

1. Update the directory values in prepare_python_env.sh
2. Run prepare_python_env.sh. This will install rapid as module in the virtual environment.
3. Render the configurations into PROXCONF dir - /tmp/prox. If u modify this, you may have to modify the hardcoded value in *prox.py* in tools/pkt_gen/prox folder.
4. start the virtual env - source VINEPROXENV_DIR/bin/activate
5. run *vineprox.py*  in VINPROX_DIR.
