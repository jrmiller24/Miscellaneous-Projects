Sub StockVolume()

    ' Set an initial variable for holding Ticker abbreviation
            Dim Ticker As String
    
    ' Set an intitial variable for holding Total Value of each Ticker symbol
            Dim TotalVolume As Double
            TotalVolume = 0

    ' Keep track of the location for each ticker symbol in the summary table
            Dim Summary_Table_Row As Integer
            Summary_Table_Row = 2
          
    ' Define worksheets for all 7 alphaebetical tabs
            Dim ws As Worksheet
    
    ' Loop for each worksheets
            For Each ws In Worksheets
        
                Lastrow = ws.Cells(Rows.Count, 1).End(xlUp).Row
            
                ws.Range("i1") = "Ticker"
                ws.Range("j1") = "Total Volume"
      
    
            ' Loop through all stock tickers
                For i = 2 To Lastrow

                    ' Check if we have changed stock ticker symbols within data, if so....

                        If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
        
                        ' Set the Stock Ticker Symbol
                            Ticker = ws.Cells(i, 1).Value
            
                        ' Add Volume to Stock Ticker Total
                            TotalVolume = TotalVolume + ws.Cells(i, 7).Value
            
                    ' Put the Ticker Symbol in Summary Table
                        ws.Range("I" & Summary_Table_Row).Value = Ticker
        
                    ' Put the Total Value of each Ticker in Summary Table
                        ws.Range("J" & Summary_Table_Row).Value = TotalVolume
        
                    ' Add a new row for new Ticker Symbol to Summary Table Row
                        Summary_Table_Row = Summary_Table_Row + 1
            
                    ' Reset TotalValue
                        TotalVolume = 0
            
        
                ' If the Ticker equals the Ticker of prior cell...
                    Else
    
                ' Add Volume to Ticker's Total Value
                    TotalVolume = TotalVolume + ws.Cells(i, 7).Value
        
                    End If
        
                Next i
                    Summary_Table_Row = 2
            Next ws
    
End Sub
