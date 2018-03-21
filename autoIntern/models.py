# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    displayName = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    title = models.CharField(max_length=255)


# class Group(models.Model):
# do we want to complicate this by adding the extra layer?? My vote is no

class Document(models.Model):
    doc_id = models.CharField(max_length=255, primary_key=True)
    company = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=255)
    doc_date = models.CharField(max_length=255)
    upload_id = models.ForeignKey(User,on_delete=models.CASCADE)
    upload_datetime = models.DateTimeField(auto_now_add = True)
    file = models.FileField(upload_to= 'document_folder')
    # pointer = models.FilePathField(......)
    #
    # def GetDocByID(id):
    #   return(Document.doc_id)


# class Case(models.Model):
#     case_id = models.CharField(max_length=255, primary_key=True)
#     creator_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     create_datetime = models.DateTimeField(auto_now_add = True)
    #


#
# class Case_File(models.Model):
#     documents = models.ManyToManyField(Documents)
#     case = models.ForeignKey(Case, on_delete = models.CASCADE)
#     #
#     #
#
#
# class Permission(models.Model):
#     user_id = models.ManyToManyField(Users)
#     case_id = models.ForeignKey(Cases, on_delete=models.CASCADE)
#     #
#     #
#
# class Data(models.Model):
#     data_id = models.CharField(max_length=255, primary_key=True)
#     creator_id = models.ForeignKey(User, on_delete= models.CASCADE)
#     case = models.ForeignKey(Cases, on_delete=models.CASCADE)
#     document = models.ForeignKey(Documents , on_delete= models.CASCADE)
#     create_datetime = models.DateTimeField.auto_now_add
#     value = models.CharField(max_length=255)
#     label = models.CharField(max_length=255)
#     line = models.CharField(max_length=255)
#     index = models.CharField(max_length=255)
#     current = models.BinaryField






#Commenting this out as it is from the demo project. Keeping it in case it is useful
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#####################################################