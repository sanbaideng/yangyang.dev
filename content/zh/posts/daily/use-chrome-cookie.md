---
title: "Bigtable"
date: 2023-06-27T09:50:12+08:00
draft: false
tags: ["Bigtable", "daily"]

---
##### What is Bigtable?
Bigtable is a distributed storage system for managing structured data that can scale to petabytes of data across thousands of commodity servers. It is used by many Google products including web indexing, Google Earth, and Google Finance.

##### What is the data model used by Bigtable?
Bigtable uses a sparse, distributed, persistent multi-dimensional sorted map that is indexed by a row key, column key, and a timestamp. Each value in the map is an uninterpreted array of bytes. Data is indexed using row and column names that can be arbitrary strings.

##### What features does the Bigtable API provide?
The Bigtable API provides functions for creating and deleting tables and column families, changing cluster, table, and column family metadata, and manipulating data through atomic mutations, single-row transactions, and integer counters. It also supports the execution of client-supplied scripts in the address spaces of the servers and can be used with MapReduce for large-scale parallel computations.