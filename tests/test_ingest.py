import pandas as pd

from alberta_well_assistant.ingest import clean

def test_clean():
    raw = pd.DataFrame(
        {
            "Licensee": ["  Cenovus Energy Inc.  "],
            "Status_Mode": ["ABANDONED      "],
            "Spud_Date": ["1977-08-15"],
            "Final_Total_Depth": [1204],            
        }
    )
    out = clean(raw)
    
    assert list(out.columns) == [
        "licensee",
        "status_mode",
        "spud_date",
        "final_total_depth",        
    ]
    assert out.loc[0, "licensee"] == "Cenovus Energy Inc."
    
    assert out.loc[0, "status_mode"] == "ABANDONED"
    
    assert pd.api.types.is_datetime64_any_dtype(out["spud_date"])
    
    assert out.loc[0, "final_total_depth"] == 1204