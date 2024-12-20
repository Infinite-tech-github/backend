## Overview

You are tasked with creating a table to organize and display data. Follow the instructions to format the data into columns and rows.

## Task Format

Deliver your table creation instructions in the following JSON structure:

```json
{
      "headers": ["Column 1 Title", "Column 2 Title", "Column 3 Title"],
      "rows": [
        {"columns": ["Data 1 Column 1", "Data 1 Column 2", "Data 1 Column 3"]},
        {"columns": ["Data 2 Column 1", "Data 2 Column 2", "Data 2 Column 3"]},
        {"columns": ["Data 3 Column 1", "Data 3 Column 2", "Data 3 Column 3"]}
      ]
  }
```

IMPORTANT: RESPOND STARTING AND ENDING WITH THE THREE BACKTICKS ```json