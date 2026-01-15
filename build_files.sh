# build_files.sh
echo "Installing requirements..."
python3 -m pip install -r requirements.txt
echo "Collecting static files..."
python3 manage.py collectstatic --noinput
echo "Build finished."
