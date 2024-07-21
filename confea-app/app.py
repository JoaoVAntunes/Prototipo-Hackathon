from controllers.app_controller import create_app

if __name__ == "__main__":
    app = create_app()
    print("Criando o App!")
    app.run(host='0.0.0.0', port=8080, debug=True)

# Debug=False > evita a duplicação dos dados 
