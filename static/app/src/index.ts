import { PlotData, PlotTrace, setPlotTraces } from "./plotUtils"
import { getTempHumidMeasData } from "./temperHumidApiUtils"

const ServerRoomTmpPnt = { id: "Server_Room|Temperature", name: 'Server Room' }
const CommRoomTmpPnt = { id: "Communication_Room|Temperature", name: 'Communication Room' }
const UpsRoomTmpPnt = { id: "UPS_Room|Temperature", name: 'UPS Room' }

const ServerRoomHumidPnt = { id: "Server_Room|Humidity", name: 'Server Room' }
const CommRoomHumidPnt = { id: "Communication_Room|Humidity", name: 'Communication Room' }
const UpsRoomHumidPnt = { id: "UPS_Room|Humidity", name: 'UPS Room' }

let intervalID = null

window.onload = async () => {
    intervalID = setInterval(refreshData, 1000 * 60 * 5);
    (document.getElementById('refreshBtn') as HTMLButtonElement).onclick = refreshData;
    refreshData()
}

const refreshData = async () => {
    const nowTime = new Date()
    const daysOffset = +((document.getElementById('daysOffsetInp') as HTMLInputElement).value);
    const startDate = new Date(nowTime.getTime() - daysOffset * 24 * 60 * 60 * 1000)
    const endDate = nowTime
    const tempTracePnts = [ServerRoomTmpPnt, CommRoomTmpPnt, UpsRoomTmpPnt]
    let plotData: PlotData = {
        title: 'Temperature monitoring',
        traces: []
    }
    for (let traceInd = 0; traceInd < tempTracePnts.length; traceInd++) {
        const tracePnt = tempTracePnts[traceInd]
        let fetchedMeasData = await getTempHumidMeasData(tracePnt.id, startDate, endDate);
        let traceObj: PlotTrace = {
            data: fetchedMeasData,
            title: tracePnt.name
        }
        plotData.traces.push(traceObj)
    }
    // render plot data
    setPlotTraces("temperDiv", plotData);

    const humTracePnts = [ServerRoomHumidPnt, CommRoomHumidPnt, UpsRoomHumidPnt]
    plotData = {
        title: 'Humidity monitoring',
        traces: []
    }
    for (let traceInd = 0; traceInd < tempTracePnts.length; traceInd++) {
        const tracePnt = humTracePnts[traceInd]
        let fetchedMeasData = await getTempHumidMeasData(tracePnt.id, startDate, endDate);
        let traceObj: PlotTrace = {
            data: fetchedMeasData,
            title: tracePnt.name
        }
        plotData.traces.push(traceObj)
    }
    // render plot data
    setPlotTraces("humidDiv", plotData);
}