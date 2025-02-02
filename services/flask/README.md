## Application FLASK 

### Post

```bash
# clé : moman, valeur : 17
curl -X POST http://0.0.0.0:5000/kv/1/moman/17

# clé : popa, valeur : 10
curl -X POST http://0.0.0.0:5000/kv/1/popa/10
```

### Get

```bash
# clé : moman
curl -X GET http://0.0.0.0:5000/kv/1/moman
# 17

# clé : popa
curl -X GET http://0.0.0.0:5000/kv/1/popa
# 10
```
