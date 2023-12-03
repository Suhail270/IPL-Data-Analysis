from Functions.cw_requirements import (doc_to_visitor, 
                              also_likes, 
                              views_country, 
                              group_country, 
                              format_browser, 
                              view_broswer, 
                              read_file,
                              visitor_to_doc,
                              avid_readers)

from Functions.additional import (max_unique_visitors, 
                         also_likes_testing, 
                         sortingfunc_test, 
                         find_doc,
                         validation)

from Functions.graphs import (countries_histogram, 
                     continents_histogram, 
                     browser_histogram,
                     format_browser_histogram)

from Functions.gui import startGUI

import pytest

# Testing if exception is raised when an invalid file path is entered.
def testInvalidFilePath():

   file_path = '/Dataset/sample_small.json'

   with pytest.raises(Exception, match="File does not exist at specified location."):
      read_file(file_path+"abc")

# Testing if exception is raised when an invalid document UUID is entered.
def testInvalidDocId():

   file_path = 'DataAnalysis/Dataset/sample_small.json'
   doc_uuid = '123'

   with pytest.raises(Exception, match="Invalid document UUID. Please try again."):
      documents, _, _ = read_file(file_path)
      validation(doc_uuid=doc_uuid, documents=documents)

# Testing if exception is raised when an invalid visitor UUID is entered.
def testInvalidVisitorId():

   file_path = 'DataAnalysis/Dataset/sample_small.json'
   visitor_uuid = '123'

   with pytest.raises(Exception, match="Invalid visitor UUID. Please try again."):
      _, visitors, _ = read_file(file_path)
      validation(visitor_uuid=visitor_uuid, visitors=visitors)

# Asserting true if valid document UUID is entered.
def testValidDocId():

   file_path = 'DataAnalysis/Dataset/sample_small.json'
   doc_uuid = '140224093301-60151c849f742e45bfb63d18ab9ded78'
   documents, _, _ = read_file(file_path)

   assert validation(doc_uuid=doc_uuid, documents=documents), True

# Asserting true if valid visitor UUID is entered.
def testValidVisitorId():

   file_path = 'DataAnalysis/Dataset/sample_small.json'
   visitor_uuid = '849bb060cb110347'
   _, visitors, _ = read_file(file_path)

   assert validation(visitor_uuid=visitor_uuid, visitors=visitors), True

def testAvidReaders():

   file_path = 'DataAnalysis/Dataset/sample_small.json'

   _, visitors, _ = read_file(file_path)
   top_10, values = avid_readers(visitors)

   assert all(values[i] >= values[i + 1] for i in range(len(values) - 1)), True

# Testing if also_likes functionality works correctly.
def testAlsoLikes():
   
      file_path = 'DataAnalysis/Dataset/sample_small.json'
      doc_uuid = '130323125939-5f4318404cda4025a2463c66435ad7c8'
      documents, _, _ = read_file(file_path)

      assert len(list(also_likes(documents, doc_uuid).keys())) > 1

