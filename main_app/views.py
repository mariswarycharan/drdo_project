from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.views import View
from django.core.files.storage import FileSystemStorage


def home(request):
  return render(request,"home.html")

import pyxtf,os
import pandas as pd
import ydata_profiling as data_vistualize

class FileUploadView(View):
    def post(self, request):
        uploaded_file = request.FILES['file']  # Assuming you're sending the file in a POST request with key 'file'
        fs = FileSystemStorage()
        filename = fs.save("input_xtf_file.xtf", uploaded_file)
  
        input_file = r'media/input_xtf_file.xtf'
        (file_header, packets) = pyxtf.xtf_read(input_file)
        attributes = {'MagicNumber': [], 'HeaderType': [], 'SubChannelNumber': [], 'NumChansToFollow': [], 'Reserved1': [], 'NumBytesThisRecord': [], 'Year': [], 'Month': [], 'Day': [], 'Hour': [], 'Minute': [], 'Second': [], 'HSeconds': [], 'JulianDay': [], 'EventNumber': [], 'PingNumber': [], 'SoundVelocity': [], 'WaterTemperature': [], 'Pressure': [], 'ComputedSoundVelocity': [], 'MagX': [], 'MagY': [], 'MagZ': [], 'AuxVal1': [], 'AuxVal2': [], 'AuxVal3': [], 'AuxVal4': [], 'AuxVal5': [], 'AuxVal6': [], 'SpeedLog': [], 'Turbidity': [], 'ShipSpeed': [], 'ShipGyro': [], 'ShipYcoordinate': [], 'ShipXcoordinate': [], 'ShipAltitude': [], 'ShipDepth': [], 'FixTimeHour': [], 'FixTimeMinute': [], 'FixTimeSecond': [], 'FixTimeHsecond': [], 'SensorSpeed': [], 'SensorYcoordinate': [], 'SensorXcoordinate': [], 'SonarStatus': [], 'RangeToFish': [], 'BearingToFish': [], 'CableOut': [], 'Layback': [], 'CableTension': [], 'SensorDepth': [], 'SensorPrimaryAltitude': [], 'SensorAuxAltitude': [], 'SensorPitch': [], 'SensorRoll': [], 'SensorHeading': [], 'Heave': [], 'Yaw': [], 'AttitudeTimeTag': [], 'NavFixMilliseconds': [], 'ComputerClockHour': [], 'ComputerClockMinute': [], 'ComputerClockSecond': [], 'ComputerClockHsec': [], 'FishPositionDeltaX': [], 'FishPositionDeltaY': [], 'FishPositionErrorCode': [], 'OptionalOffset': [], 'CableOutHundredths': [], 'ReservedSpace2': [], 'data': []}
        dataframe = pd.DataFrame(attributes)
        list_data = []
        for i in packets[0]:
            list_data.append([i.MagicNumber, i.HeaderType, i.SubChannelNumber, i.NumChansToFollow, i.Reserved1, i.NumBytesThisRecord, i.Year, i.Month, i.Day, i.Hour, i.Minute, i.Second, i.HSeconds, i.JulianDay, i.EventNumber, i.PingNumber, i.SoundVelocity, i.WaterTemperature, i.Pressure, i.ComputedSoundVelocity, i.MagX, i.MagY, i.MagZ, i.AuxVal1, i.AuxVal2, i.AuxVal3, i.AuxVal4, i.AuxVal5, i.AuxVal6, i.SpeedLog, i.Turbidity, i.ShipSpeed, i.ShipGyro, i.ShipYcoordinate, i.ShipXcoordinate, i.ShipAltitude, i.ShipDepth, i.FixTimeHour, i.FixTimeMinute, i.FixTimeSecond, i.FixTimeHsecond, i.SensorSpeed, i.SensorYcoordinate, i.SensorXcoordinate, i.SonarStatus, i.RangeToFish, i.BearingToFish, i.CableOut, i.Layback, i.CableTension, i.SensorDepth, i.SensorPrimaryAltitude, i.SensorAuxAltitude, i.SensorPitch, i.SensorRoll, i.SensorHeading, i.Heave, i.Yaw, i.AttitudeTimeTag, i.NavFixMilliseconds, i.ComputerClockHour, i.ComputerClockMinute, i.ComputerClockSecond, i.ComputerClockHsec, i.FishPositionDeltaX, i.FishPositionDeltaY, i.FishPositionErrorCode, i.OptionalOffset, i.CableOutHundredths, i.ReservedSpace2, i.data])
            
        result_df = pd.DataFrame(data=list_data,columns=['MagicNumber', 'HeaderType', 'SubChannelNumber', 'NumChansToFollow', 'Reserved1', 'NumBytesThisRecord', 'Year', 'Month', 'Day', 'Hour', 'Minute', 'Second', 'HSeconds', 'JulianDay', 'EventNumber', 'PingNumber', 'SoundVelocity', 'WaterTemperature', 'Pressure', 'ComputedSoundVelocity', 'MagX', 'MagY', 'MagZ', 'AuxVal1', 'AuxVal2', 'AuxVal3', 'AuxVal4', 'AuxVal5', 'AuxVal6', 'SpeedLog', 'Turbidity', 'ShipSpeed', 'ShipGyro', 'ShipYcoordinate', 'ShipXcoordinate', 'ShipAltitude', 'ShipDepth', 'FixTimeHour', 'FixTimeMinute', 'FixTimeSecond', 'FixTimeHsecond', 'SensorSpeed', 'SensorYcoordinate', 'SensorXcoordinate', 'SonarStatus', 'RangeToFish', 'BearingToFish', 'CableOut', 'Layback', 'CableTension', 'SensorDepth', 'SensorPrimaryAltitude', 'SensorAuxAltitude', 'SensorPitch', 'SensorRoll', 'SensorHeading', 'Heave', 'Yaw', 'AttitudeTimeTag', 'NavFixMilliseconds', 'ComputerClockHour', 'ComputerClockMinute', 'ComputerClockSecond', 'ComputerClockHsec', 'FishPositionDeltaX', 'FishPositionDeltaY', 'FishPositionErrorCode', 'OptionalOffset', 'CableOutHundredths', 'ReservedSpace2', 'data'])
        
        result_df = result_df.iloc[:,:-1]
        profile = data_vistualize.ProfileReport(result_df)
        profile.to_file("main_app/templates/output.html")
        
        os.remove(r"media\input_xtf_file.xtf")
        return render(request,"output.html")
