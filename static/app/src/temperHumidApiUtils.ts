import { PlotTrace } from "./plotUtils";
import { convertDateTimeToUrlStr } from "./timeUtils";

export const getTempHumidMeasData = async (measId: string, startDate: Date, endDate: Date): Promise<PlotTrace["data"]> => {
    try {
        const startDateStr = convertDateTimeToUrlStr(startDate)
        const endDateStr = convertDateTimeToUrlStr(endDate)
        const resp = await fetch(`../api/${measId}/${startDateStr}/${endDateStr}`, {
            method: 'get'
        });
        const respJSON = await resp.json() as PlotTrace["data"];
        return respJSON;
    } catch (e) {
        console.error(e);
        return [];
    }
};