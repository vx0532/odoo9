# -*- coding: utf-8 -*-
from openerp import models, fields, api,exceptions
import base64,io,pandas,os #,StringIO,openpyxl,xlrd
import Image,cv2


class ColorTask(models.Model):
    _name = 'color.task'
    _description = 'Color task'
    datafile=fields.Binary(u'请选择图片',required=True)
    redvalue=fields.Float(u'色价量化值')

    @api.multi
    def colorread(self,cr):
      file_like=io.BytesIO(base64.b64decode(self.datafile))
      im=Image.open(file_like)
      width=im.size[0]
      length=im.size[1]
      value=0.0;
      for i in range(0,width):
        for j in range(0,length):
          value=value+im.getpixel((i,j))[0]
      value=value/(i*j)
      self.redvalue=value/255
      



    




