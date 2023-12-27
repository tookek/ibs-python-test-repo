from fastapi import FastAPI, HTTPException, File, UploadFile
from typing import List, Dict
import json
from pydantic import BaseModel
from Converter_Integer_to_Roman.int_to_roman import int_to_roman
from Pandas_and_csv.parse_scv import average_age_by_position
from Filtering_an_array_based_on_string_case.find_different_regs import find_in_different_registers


class Words(BaseModel):
    words: List[str]


class InputData(BaseModel):
    number: int


app = FastAPI()


@app.post("/average_age_by_position/")
async def calculate_average_age(file: UploadFile = File(...)) :
    try:
        contents = await file.read()
        result = average_age_by_position(contents)

        return json.dumps(result, indent=4, ensure_ascii=False)

    except Exception as e:
        raise HTTPException(status_code=400, detail='Invalid file')


@app.post("/find_in_different_registers", response_model=List[str])
async def find_unique_words(words: Words):
    try:
        input_words = words.words
        print(input_words)
        unique_words = find_in_different_registers(input_words)
        return unique_words
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/int_to_roman", response_model=Dict[str, str])
def convert_to_roman(data: InputData):
    result = int_to_roman(data.number)
    return {"roman_number": result}