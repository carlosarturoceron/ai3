import os
import requests
import tensorflow as tf

class Retriever:

    def get_h5_model(self, modelName, cid):

        # IPFS API endpoint
        api_endpoint = f"https://{cid}.ipfs.w3s.link/ipfs/{cid}/{modelName}.h5"

        try:
            # Get the current directory
            current_dir = os.getcwd()

            # Construct the file path in the 'models' directory
            models_dir = os.path.join(current_dir, "models")
            os.makedirs(models_dir, exist_ok=True)

            # Construct the file path for the model
            file_path = os.path.join(models_dir, f"{modelName}.h5")

            # Fetch the file from IPFS
            response = requests.get(api_endpoint)
            if response.status_code == 200:
                # Write the response content to the file
                with open(file_path, "wb") as f:
                    f.write(response.content)
                
                print("File fetched successfully from IPFS and saved at:", file_path)

                # Load the model and return it
                loaded_model = tf.keras.models.load_model(file_path)
                return loaded_model
            else:
                print("Error fetching file from IPFS. Status code:", response.status_code)
                return None
        except Exception as e:
            print("Error:", e)
            return None

