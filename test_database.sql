--
-- PostgreSQL database dump
--

-- Dumped from database version 12.13 (Ubuntu 12.13-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.13 (Ubuntu 12.13-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: test
--

COPY public.alembic_version (version_num) FROM stdin;
401f15e96957
\.


--
-- Data for Name: todo; Type: TABLE DATA; Schema: public; Owner: test
--

COPY public.todo (id, content, completed, date_created) FROM stdin;
17	do the dishes	\N	2024-02-17 13:53:10.23593
16	clean the house today	\N	2024-02-17 13:43:07.728308
18	take the dog for a walk in the evening, 4pm	\N	2024-02-17 15:22:09.182109
\.


--
-- Name: todo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: test
--

SELECT pg_catalog.setval('public.todo_id_seq', 18, true);


--
-- PostgreSQL database dump complete
--

