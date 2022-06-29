from blog import app
import redis

cache = redis.Redis(host="redis", port=6379)

if __name__ == "__main__":
    app.run(debug=True)