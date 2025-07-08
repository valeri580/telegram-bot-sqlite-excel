--
-- PostgreSQL database dump
--

-- Dumped from database version 16.8
-- Dumped by pg_dump version 17.5

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: users; Type: TABLE; Schema: public; Owner: valeri580_admin
--

CREATE TABLE public.users (
    id integer NOT NULL,
    "full-name" text NOT NULL,
    summ real DEFAULT 0 NOT NULL,
    card_number integer,
    birthday date
);


ALTER TABLE public.users OWNER TO valeri580_admin;

--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: valeri580_admin
--

COPY public.users (id, "full-name", summ, card_number, birthday) FROM stdin;
1	Петров Иван Иванович	600	2220	2001-01-11
0	Иванов Иван Иванович	500	3330	2001-01-01
\.


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: valeri580_admin
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

