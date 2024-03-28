import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.previous_hash, timestamp, data)
    return Block(index, previous_block.previous_hash, timestamp, data, hash)

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Ajouter de nouveaux blocs à la blockchain
for i in range(1, 10):
    block_data = f"Block Data {i}"
    new_block = create_new_block(previous_block, block_data)
    blockchain.append(new_block)
    previous_block = new_block

# Générer le code HTML pour la table
table_rows = ""
for block in blockchain:
    table_rows += f"<tr><td>{block.index}</td><td>{block.previous_hash}</td><td>{block.timestamp}</td><td>{block.data}</td><td>{block.hash}</td></tr>"

# Écrire le code HTML dans un fichier
with open("index.html", "w") as f:
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")
    f.write("<head>\n")
    f.write("    <title>Blockchain</title>\n")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write("    <h1>Blockchain</h1>\n")
    f.write("    <table border=\"1\">\n")
    f.write("        <tr>\n")
    f.write("            <th>Index</th>\n")
    f.write("            <th>Previous Hash</th>\n")
    f.write("            <th>Timestamp</th>\n")
    f.write("            <th>Data</th>\n")
    f.write("            <th>Hash</th>\n")
    f.write("        </tr>\n")
    f.write(table_rows)
    f.write("    </table>\n")
    f.write("</body>\n")
    f.write("</html>\n")