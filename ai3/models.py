from .utils.load import Retriever

class spamDetection:

    @staticmethod
    def load():
        storage = Retriever()
        # Example CID for the model on IPFS
        model_name = "spamDetection"
        cid = "bafybeibpfdw6stsf3leqj3a3fvwsx7bzjahifbnuy2adofhkfif7nwmyrq"
        # Example transaction ID for the model on Arweave
        return storage.get_h5_model(model_name, cid)

class imageNet:

    @staticmethod
    def load():
        storage = Retriever()
        # Example CID for the model on IPFS
        model_name = "imageNet"
        cid = "bafybeif6torjb3t7wha56go3a6yullryafdctg2ipz5rxi5azjmgolx23e"
        # Example transaction ID for the model on Arweave
        return storage.get_h5_model(model_name, cid)
