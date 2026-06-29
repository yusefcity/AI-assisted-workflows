# Contract Signing Engine with AI-assisted workflow
import hashlib
import json
import time
from datetime import datetime

class ContractEngine:
    def __init__(self):
        self.history = []

    def build_contract(self, sender, receiver, payload):
        return {
            "sender": sender,
            "receiver": receiver,
            "payload": payload,
            "timestamp": time.time()
        }

    def serialize(self, contract):
        return json.dumps(contract, sort_keys=True)

    def hash_contract(self, contract_str):
        return hashlib.sha256(contract_str.encode()).hexdigest()

    def sign(self, contract_hash, secret):
        combined = f"{contract_hash}:{secret}"
        return hashlib.sha256(combined.encode()).hexdigest()

    def verify(self, contract_hash, signature, secret):
        expected = self.sign(contract_hash, secret)
        return expected == signature

    def log(self, record):
        record["logged_at"] = datetime.utcnow().isoformat()
        self.history.append(record)

def simulate_flow():
    engine = ContractEngine()
    contract = engine.build_contract("OrgA", "OrgB", "Service Agreement")
    cstr = engine.serialize(contract)
    chash = engine.hash_contract(cstr)
    sig = engine.sign(chash, "key123")
    engine.log({"hash": chash, "signature": sig})
    print("Hash:", chash)
    print("Signature:", sig)
    print("Verified:", engine.verify(chash, sig, "key123"))
    print("History size:", len(engine.history))
    return engine
