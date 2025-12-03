from main import app

# Expose a WSGI callable named `application` so WSGI servers
# (including Gunicorn) can import the app as a module-level object.
application = app

if __name__ == "__main__":
	# When run directly, start Flask's development server for convenience.
	app.run(host="0.0.0.0", port=8000, debug=True)