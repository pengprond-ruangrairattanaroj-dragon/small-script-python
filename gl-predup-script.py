
import json
from os import listdir
from os.path import isfile, join
import pandas as pd

path_to_save = "/Users/pengprond.ruangrairattanaroj/Documents/gl_derived_pre_dedup_20221228.csv"
df_posting = pd.read_csv(path_to_save)
df_posting = df_posting[df_posting["client_id"] == "casemgmt"]




json_path = '/Users/pengprond.ruangrairattanaroj/Downloads/json'

onlyfiles = [f for f in listdir(json_path) if isfile(join(json_path, f))]
df_posting_copy = df_posting.copy()

for i in onlyfiles:
    if ".json" in i:
        f = json_path + "/" + i
        data_q = pd.read_json(f, lines=True)

        data = pd.io.json.json_normalize(data_q["msg_payload"])
        data = data[data["posting_instruction_batch.client_id"]=="casemgmt"]


        for index, row in data.iterrows():
            if "transfer_msg" in row["posting_instruction_batch.posting_instructions"][0]["instruction_details"]:
                data.loc[index, 'transfer_msg'] = row["posting_instruction_batch.posting_instructions"][0]["instruction_details"]["transfer_msg"]
                df_posting.loc[df_posting["client_batch_id"] == row["posting_instruction_batch.client_batch_id"], 'memo'] = "casemgmt::"+row["posting_instruction_batch.posting_instructions"][0]["instruction_details"]["transfer_msg"]
            elif "transfer_reason" in row["posting_instruction_batch.posting_instructions"][0]["instruction_details"]:
                data.loc[index, 'transfer_reason'] = row["posting_instruction_batch.posting_instructions"][0]["instruction_details"]["transfer_reason"]
                df_posting.loc[df_posting["client_batch_id"] == row["posting_instruction_batch.client_batch_id"], 'memo'] = "casemgmt::"+row["posting_instruction_batch.posting_instructions"][0]["instruction_details"]["transfer_reason"]
            df_posting_copy = df_posting



print("completed result: ")
df_posting_copy.to_csv(path_to_save,index=False)