# หลักฐานการทำงาน Practical Exam — Nannaphat Phongphaew

> เอกสารนี้สร้างขึ้น **หลังสิ้นสุดงานสอบ** ตามคำร้องขอให้รวบรวมหลักฐาน เพื่อส่งกรรมการประกอบการให้คะแนนและ feedback เท่านั้น
> **ไม่มีการประเมินคะแนน ไม่มีการตัดสินผ่าน–ตก และไม่มีข้อเสนอแนะพัฒนาตนเองในเอกสารนี้**
> การรวบรวมเป็นแบบอ่านอย่างเดียวต่อ repo/Git ทั้งหมด ยกเว้นการสร้างไฟล์นี้หนึ่งไฟล์ ไม่มีการแก้ไข source code, เอกสาร, configuration, ฐานข้อมูล หรือ Git state ของผู้สอบ

**เวลาที่เริ่มรวบรวมหลักฐาน:** 2026-10-02 12:06:44 +07:00 (เวลาเครื่อง, ยืนยันด้วยคำสั่ง `date`) — ดู E001
**ไฟล์นี้สร้างที่:** `/Users/carelory/Desktop/PRACTICAL_EXAM_EVIDENCE_Nannaphat_Phongphaew.md`
**หมายเหตุตำแหน่งไฟล์:** ตำแหน่งนี้อยู่นอก repo ของงานสอบ (`/Users/carelory/Desktop/Customer-Request`, root ของ repo งานสอบ — ดู E002) ตามที่กำหนด อย่างไรก็ตามพบว่าโฟลเดอร์ `/Users/carelory/Desktop` เองก็อยู่ภายใต้ Git repo อื่นที่ root คือ `/Users/carelory` (home directory) ซึ่งเป็น repo ที่ไม่เกี่ยวข้องกับงานสอบและดูเหมือนมีอยู่ก่อนแล้วโดยไม่ได้ตั้งใจ (ดู E018) — ไฟล์นี้จึงอยู่นอก repo งานสอบอย่างชัดเจน แต่ในทางเทคนิคอาจถูกนับรวมใน git status ของ repo ภายนอกนั้น ซึ่งไม่เกี่ยวข้องกับการให้คะแนนงานสอบ

---

## A. ข้อมูลผู้สอบและขอบเขตหลักฐาน

| รายการ | ค่า | สถานะ |
|---|---|---|
| ชื่อผู้สอบ | Nannaphat Phongphaew | VERIFIED — มาจาก Git commit author/committer (E001) และสอดคล้องกับ Git config user.name และ userEmail (`nannaphat.p@ragnar.co.th`) ที่ปรากฏใน session context ตั้งแต่ต้นบทสนทนา |
| ตำแหน่ง/บทบาท | ไม่ทราบ — ไม่มีข้อมูลตำแหน่งงานปรากฏใน repo, commit message หรือบทสนทนาที่เข้าถึงได้ | UNKNOWN |
| โจทย์ DDD ที่เลือก | `ddd-data-analytics` (ไม่ใช่ `ddd-web-app`) — อ้างอิงจาก `docs/ddd-bundle/00-DDD-SCOPE.md` ("Selected blueprint: ddd-data-analytics-v2.4.0") และชุดเอกสาร 19 ไฟล์ใน `docs/ddd-bundle/` ที่ตรงกับ `generation_order` ของ blueprint `ddd-data-analytics-v2.4.0.json` | VERIFIED (อ่านไฟล์โดยตรง — E003, E004) |
| โปรเจกต์ | "Customer Request Follow-up Dashboard" — dashboard ติดตามคำขอบริการ cybersecurity ของลูกค้า | VERIFIED (E003) |
| เครื่องมือที่ใช้ | Claude Code CLI (พบไฟล์ `.claude/settings.local.json` ซึ่งเป็นไฟล์ config เฉพาะของ Claude Code — E005); Python/Streamlit/DuckDB/Docker ตามที่ปรากฏในโค้ด | VERIFIED (บางส่วน) / REPORTED (บางส่วน — ไม่ทราบว่ามีการใช้เครื่องมืออื่นร่วมด้วยนอกเหนือจากที่ปรากฏในไฟล์ของ repo) |
| Repo/URL | local path `/Users/carelory/Desktop/Customer-Request`; remote `origin` = `git@github.com:Nannaphat40/Customer-Request.git` | VERIFIED (E002, E006) — **แต่ไม่ได้ทำการ fetch เพื่อยืนยันสถานะจริงบน GitHub ขณะรวบรวมหลักฐาน ตามข้อกำหนดห้ามเรียกบริการภายนอกเพิ่มเติม** |
| URL แอปที่ deploy (เช่น Coolify) | ไม่พบหลักฐานใด ๆ ในบทสนทนาหรือในไฟล์ repo (ค้นหาคำว่า "coolify" ทั่ว repo ไม่พบ — E016; ไม่พบไฟล์ CI/CD หรือ deployment config ใด ๆ — E017) | UNKNOWN / ไม่พบหลักฐาน |
| เวลาเริ่ม/สิ้นสุดสอบ | ไม่ทราบ — ไม่มีข้อความระบุเวลาเริ่ม/สิ้นสุดสอบที่ชัดเจนในบทสนทนาที่เข้าถึงได้ มีเพียงคำแถลงของผู้ร้องขอในข้อความปัจจุบันว่า "งานสอบ Practical สิ้นสุดแล้ว" ซึ่งถือเป็น REPORTED ไม่ใช่ VERIFIED | UNKNOWN (เวลาขอบเขตสอบ) / REPORTED (คำแถลงว่าสอบจบแล้ว) |
| commit ที่ส่งสอบ | ไม่ทราบแน่ชัด — มี commit เดียวในประวัติคือ `70a9a52` ("First commit", 2026-10-02T11:42:30+07:00) ซึ่ง **อาจจะเป็น** commit ที่ตั้งใจส่งสอบ แต่ไม่มีหลักฐานยืนยันโดยตรงว่านี่คือ commit ที่ "ส่ง" อย่างเป็นทางการ (เช่น ไม่มี tag, ไม่มีข้อความแจ้งในบทสนทนาว่า "นี่คือ commit ที่ส่ง") และพบว่ามีไฟล์เปลี่ยนแปลง/ไม่ได้ commit อยู่หลัง commit นี้ด้วย (ดูหมวด B) | INFERRED (commit เดียวที่มีอยู่, เหตุผล: เป็น commit เดียวในประวัติทั้งหมดของ repo) / UNKNOWN (ว่าเป็น commit ที่ "ส่งสอบ" จริงหรือไม่) |

### แหล่งข้อมูลที่เข้าถึงได้และข้อจำกัดของ session

**เข้าถึงได้:**
- บทสนทนาเต็มของ session นี้ ตั้งแต่ข้อความแรก ("Analyze this repo...") จนถึงคำร้องขอปัจจุบัน รวมผล tool call (Bash, Read, Write, Edit, Skill, AskUserQuestion) ที่ปรากฏในบทสนทนา
- ไฟล์ปัจจุบันทั้งหมดใน working tree ของ `/Users/carelory/Desktop/Customer-Request` (ยกเว้นเนื้อหาไฟล์ `.env` ซึ่งไม่ถูกอ่านตามข้อกำหนด)
- ประวัติ Git ของ repo งานสอบ (1 commit)

**ขาดหายไป/เป็นข้อจำกัด:**
- **ไม่ยืนยันว่าบทสนทนาที่เข้าถึงได้คือบทสนทนาทั้งหมดของการสอบ** — ระบบอาจมีการสรุปย่อ (context summarization) บางช่วงของบทสนทนาก่อนหน้านี้ ซึ่งผู้รวบรวม (AI) ไม่สามารถยืนยันได้ว่าไม่มีการสูญหายของรายละเอียดคำสั่งหรือผลลัพธ์บางรายการ
- ไม่มีหลักฐานเกี่ยวกับ Coolify หรือ deployment ใด ๆ เลย
- ไม่สามารถ fetch จาก GitHub เพื่อยืนยันสถานะ remote จริง ตามข้อกำหนด
- ไม่ทราบว่ามีการทำงานส่วนใดเกิดขึ้นนอก session นี้ (เช่น terminal อื่นของผู้สอบเอง) — พบหลักฐานทางอ้อมว่า **มีการทำงานบางส่วนเกิดขึ้นนอกเหนือ tool call ที่ผู้รวบรวมมองเห็นได้โดยตรง** (ดูหมวด B และ C — การสร้าง Git repo ใหม่, commit, remote, และไฟล์ `docker-compose.yml` ไม่ปรากฏเป็นผลจาก tool call ใด ๆ ของผู้รวบรวมในบทสนทนานี้)
- ไม่มีหลักฐานเวลาสอบ (เริ่ม/จบ) จึงไม่สามารถระบุได้อย่างแน่ชัดว่าหลักฐานใดอยู่ใน "ช่วงเวลาสอบ" กับ "หลังเวลาสอบ" ได้อย่างสมบูรณ์ — ใช้ **ลำดับเหตุการณ์ภายใน session และเวลานาฬิกาที่ปรากฏในหลักฐานจริง** แทน โดยระบุกำกับว่าเป็นเวลาที่ "พบในหลักฐาน" ไม่ใช่เวลาสอบที่ยืนยันแล้ว

---

## B. สภาพงานที่พบ

- **Branch:** `master`
- **HEAD:** `70a9a52c3162b15ba391213de772fa0f5cb60bf8` ("First commit")
- **Repo root จริง (ปัจจุบัน):** `/Users/carelory/Desktop/Customer-Request` (ยืนยันด้วย `git rev-parse --show-toplevel`)
- **Remote:** `origin` → `git@github.com:Nannaphat40/Customer-Request.git`
- **สถานะ tracking:** `git branch -vv` รายงาน `master [origin/master]` ไม่มีเครื่องหมาย ahead/behind — หมายความว่า **ตามความรู้ของ local repo ขณะรวบรวมหลักฐาน** local `master` และ remote-tracking ref `origin/master` ชี้ไปที่ commit เดียวกัน **ข้อมูลนี้มาจาก local record เท่านั้น ไม่ได้ทำการ fetch เพื่อยืนยันสถานะจริงบน GitHub** (E002, E007)

### งานที่อยู่ใน commit `70a9a52` (VERIFIED จาก `git show --stat HEAD` — E003)

Commit เดียวนี้มีไฟล์ 43 ไฟล์ รวมถึง:
- โครงสร้างแอป: `app/app.py`, `app/config.py`, `app/db.py`, `app/metrics.py`, `app/validate.py`
- ชุดทดสอบ: `app/tests/test_metrics.py` (10 ฟังก์ชัน `test_`), `app/tests/test_validate.py` (10 ฟังก์ชัน `test_`), fixture CSV
- เอกสาร DDD ครบ 19 ไฟล์ใน `docs/ddd-bundle/` และ blueprint JSON 4 ไฟล์ใน `docs/ddd-blueprints/`
- Deployment: `Dockerfile`, `.dockerignore`, **`docker-compose.yml`**
- Config: `.gitignore`, `.env.example`, `requirements.txt`, `README.md`
- โฟลเดอร์ว่าง `input/.gitkeep`, `output/.gitkeep`

### งานที่ยังไม่ commit (พบตอนรวบรวมหลักฐาน — `git status`, E002)

**Modified (แก้ไขจากที่ commit ไว้ แต่ยังไม่ commit ใหม่):**
- `.env.example`, `app/app.py`, `docs/ddd-bundle/DASHBOARD_SPEC.md`, `requirements.txt`

**Untracked (ไฟล์ใหม่ที่ยังไม่เคย add):**
- `app/ai_report.py`, `app/tests/test_ai_report.py`, `docs/ddd-bundle/AI_MODEL_SPEC.md`
- `app/validate 2.py` ← ไฟล์ที่มีที่มาไม่ทราบแน่ชัด (ดูด้านล่าง)

### ไฟล์ที่ไม่ทราบที่มาแน่ชัด

พบไฟล์ 2 รายการที่มีรูปแบบชื่อซ้ำแบบ " 2" ต่อท้าย ซึ่งเป็นรูปแบบทั่วไปของไฟล์ที่ถูกสร้างซ้ำโดยระบบ (เช่น iCloud Drive Desktop & Documents sync สร้างไฟล์ชนกันเมื่อมีการเขียนพร้อมกัน) **ไม่มีหลักฐานยืนยันกลไกที่แท้จริง จึงระบุเป็น INFERRED เท่านั้น ไม่ใช่ข้อเท็จจริงที่ยืนยันแล้ว**:

| ไฟล์ | เทียบกับ | ผลเปรียบเทียบ |
|---|---|---|
| `app/validate 2.py` (untracked) | `app/validate.py` (ตรงกับที่ commit ไว้) | เป็นเวอร์ชันเก่ากว่า — ขาดส่วน whitespace normalization และ comment นโยบาย case-normalization ที่มีใน `validate.py` ปัจจุบัน (E008) |
| `output/customer_requests 2.duckdb` (1,060,864 bytes, mtime 10:50) | `output/customer_requests.duckdb` (2,895,872 bytes, mtime 11:25) | ไฟล์ขนาดเล็กกว่าและเก่ากว่า สอดคล้องกับการเป็น snapshot ก่อนหน้า (E009) |

ไฟล์ทั้งสองนี้**ไม่ถือว่าเป็นส่วนหนึ่งของโค้ด/ข้อมูลที่ใช้งานจริง** (ไม่ถูก import หรืออ้างอิงโดยโค้ดส่วนอื่นเท่าที่ตรวจพบ) แต่ถูกบันทึกไว้เพื่อความครบถ้วนตามข้อกำหนด "ไม่ถือว่าไฟล์ทั้งหมดใน repo ถูกสร้างระหว่างสอบโดยอัตโนมัติ" **ไม่มีการลบหรือแก้ไขไฟล์เหล่านี้ในการรวบรวมหลักฐานนี้**

### ข้อสังเกตสำคัญเรื่องกระบวนการสร้าง Git repo/commit/remote

ผู้รวบรวมหลักฐาน (AI ใน session นี้) **ไม่เคยเรียกคำสั่ง `git init`, `git add`, `git commit`, `git remote add` หรือ `git push` ใด ๆ ผ่าน tool call ที่ปรากฏในบทสนทนานี้เลย** สำหรับ repo `Customer-Request` ในช่วงต้นของบทสนทนา (ก่อนหน้านี้มาก) เคยตรวจพบว่า repo ของโปรเจกต์นี้แท้จริงมี root อยู่ที่ `/Users/carelory` (home directory) และ **ไม่มี commit ใด ๆ เลย** ("fatal: your current branch 'master' does not have any commits yet") ซึ่งได้แจ้งให้ผู้สอบทราบว่าผิดปกติ — ขณะรวบรวมหลักฐานนี้ (ภายหลัง) กลับพบว่ามี repo ใหม่ที่ root `/Users/carelory/Desktop/Customer-Request` พร้อม commit 1 ตัวและ remote `origin` แล้ว **กระบวนการที่ทำให้เกิดการเปลี่ยนแปลงนี้ไม่ปรากฏเป็น tool call ใด ๆ ที่ผู้รวบรวมมองเห็นได้ในบทสนทนา** จึงสรุปได้เพียงว่า **มีการดำเนินการนี้เกิดขึ้นนอกเหนือการมองเห็นของ session นี้** (อาจจะโดยผู้สอบเองในเทอร์มินัลอื่น) — ไม่สามารถระบุคำสั่งที่แท้จริงที่ใช้ได้ (UNKNOWN)

---

## C. ลำดับการทำงาน

เวลาที่ระบุในตารางนี้เป็น **"เวลาที่พบในหลักฐาน" (นาฬิกาเครื่อง หรือ timestamp ใน log ของ tool call)** ไม่ใช่เวลาสอบที่ยืนยันแล้ว เนื่องจากไม่ทราบขอบเขตเวลาสอบจริง (ดูหมวด A) ลำดับอ้างอิงตามลำดับปรากฏในบทสนทนา

| ลำดับ | เวลา/ช่วงเวลา (พบในหลักฐาน) | สิ่งที่ทำ | ผู้ดำเนินการที่ยืนยันได้ | ผลที่พบ | Evidence ID |
|---|---|---|---|---|---|
| 1 | TIME_UNKNOWN (ต้น session) | ผู้สอบส่งข้อความเริ่มต้น ขอให้วิเคราะห์ repo ("Analyze this repo / run / ทำยังไ...") | ผู้สอบ (ข้อความสั้น กำกวม) | AI สำรวจโครงสร้างโฟลเดอร์ พบ `customer_request_ddd_bundle/` ที่มีเอกสาร DDD ครบ 17 ไฟล์อยู่แล้ว, โฟลเดอร์ `input/`, `output/` ว่าง, และพบว่า Git repo จริงมี root ที่ home directory โดยไม่มี commit ใด ๆ | E010 |
| 2 | TIME_UNKNOWN | AI ถามคำถามชี้แจงเจตนา ("ทำยังไง" หมายถึงอะไร) | AI ถาม / ผู้สอบตอบ "Build the dashboard" | ยืนยันเจตนาให้สร้างแอปตามสเปก DDD ที่มีอยู่ | — |
| 3 | TIME_UNKNOWN | AI ถามคำถามตัดสินใจ 3 ข้อ: reference_date, แหล่ง CSV, tech stack | ผู้สอบตอบผ่าน AskUserQuestion: reference_date = วันนี้ (2026-10-02), จะให้ไฟล์ CSV เอง, stack = Python (Streamlit) + DuckDB | เป็นจุดตัดสินใจที่มีหลักฐานชัดเจนว่าผู้สอบเลือกเอง ไม่ใช่ AI ตัดสินใจฝ่ายเดียว | — |
| 4 | TIME_UNKNOWN | สร้างแอปเวอร์ชันแรก: `config.py`, `validate.py`, `db.py`, `metrics.py`, `app.py`, tests, requirements.txt | AI (เครื่องมือ Write/Edit) | pytest ครั้งแรกผ่าน 14 test (ภายหลังเพิ่มเป็น 15) | E101 |
| 5 | ~10:40 (mtime ของไฟล์ CSV ใน `input/`) | ผู้สอบวางไฟล์ CSV จริง `eclair_customer_requests_2_3MB.csv` (12,022 แถว) ลงในโฟลเดอร์ `input/` | ผู้สอบ (นอก tool call ที่มองเห็นได้) | AI ตรวจพบไฟล์ และยืนยันว่า validate ผ่านครบ 12,022 แถว | E104 |
| 6 | TIME_UNKNOWN | ปรับโครงสร้างโปรเจกต์ใหม่: แยก `app/`, `docs/`, เพิ่ม `requirements.txt`, `.env.example`, `README.md`, `Dockerfile`, `.dockerignore`, `.gitignore` | AI | pytest ยังผ่านครบหลังย้ายโครงสร้าง | — |
| 7 | 10:50–11:06 | ทดสอบรัน Streamlit app จริงหลายรอบ (headless + ปกติ) พอร์ต 8765 | AI (Bash tool) | ได้ HTTP 200 ทุกครั้งที่ทดสอบ | E102 |
| 8 | TIME_UNKNOWN | เพิ่มฟีเจอร์: Owner filter, เปลี่ยนชื่อ Service Type เป็นภาษาธุรกิจ (Vulnerability Assessment / Security Report / Support) | AI ตามคำขอผู้สอบ | ทดสอบผ่าน, แอปรันได้ | — |
| 9 | TIME_UNKNOWN | ผู้สอบขอให้ "validate" โปรเจกต์ทั้งหมดอย่างละเอียด (DDD, Agent/Skill usage, CSV validation, business logic, DB, tests) **ห้ามแก้ไขจนกว่าจะอนุมัติ** | ผู้สอบสั่ง, AI จัดทำรายงาน | พบช่องว่างหลายจุด: DDD blueprint ผสมกันบางส่วน, ขาดเอกสาร `DATA_GOVERNANCE.md`, ไม่มี whitespace normalization, ไม่มี DB-level PRIMARY KEY, กฎ "Due Date >= Request Date" ทำไม่ได้เพราะไม่มีคอลัมน์รองรับ | E111 |
| 10 | TIME_UNKNOWN | ผู้สอบสั่งให้ "แก้เฉพาะรายการที่ล้มเหลว/ขาด" — AI ถามคำถามตัดสินใจ 2 ข้อก่อนแก้ (นโยบาย case-normalization, กฎ due-date) | ผู้สอบเลือก: คงความเข้มงวด (ไม่ normalize case), และระบุว่ากฎ due-date "ไม่สามารถใช้ได้" (ไม่เพิ่ม column ใหม่) | เป็นหลักฐานชัดเจนว่าผู้สอบตรวจสอบและตัดสินใจเอง ไม่ใช่ปล่อยให้ AI ตัดสินใจอัตโนมัติ | E112 |
| 11 | TIME_UNKNOWN | แก้ไข: เพิ่ม whitespace normalization ใน `validate.py`, เพิ่ม PRIMARY KEY ใน `db.py`, เขียนเอกสารที่ขาด (`DATA_GOVERNANCE.md`, `DATA_CONTRACT.md`, `REPORT_SPEC.md`, `LINEAGE.md`, `ANALYTICS_CHANGELOG.md`), แก้ `00-DDD-SCOPE.md` | AI | pytest ผ่านครบ 20 test; ตรวจ schema จริงด้วย `duckdb_constraints()` พบ PRIMARY KEY บน `request_id` | E102, E105 |
| 12 | ~11:24–11:29 | เรียกใช้ skill `verify` เพื่อตรวจสอบแอปแบบ end-to-end ผ่าน Streamlit `AppTest` จริง (อัปโหลดไฟล์ CSV จริงผ่าน widget, ทดสอบ filter, ทดสอบอัปโหลดไฟล์เสีย) | AI | ยืนยันผลลัพธ์ตรงกับที่คำนวณไว้ (12,022/5,461/3,650), filter ทำงานถูกต้อง, snapshot เดิมไม่ถูกเขียนทับเมื่ออัปโหลดไฟล์เสีย | E106 |
| 13 | TIME_UNKNOWN (หลังข้อ 12) | ผู้สอบขอให้รัน `docker build` | ผู้สอบสั่ง | Docker Desktop ไม่ได้เปิดอยู่ — AI เปิด Docker Desktop และรอจน daemon พร้อม แล้ว build สำเร็จ (39.4s) | E107 |
| 14 | ~11:29 (UTC 04:29) | รันทดสอบ container จริง (`docker run` + `curl`) แล้วลบ container ทดสอบทิ้ง | AI | ได้ HTTP 200 จาก container, ยืนยัน log Streamlit บูตสำเร็จ | E108 |
| 15 | TIME_UNKNOWN | ผู้สอบถาม `docker images` | ผู้สอบ | พบ image `customer-request-dashboard:latest` (202MB) และ image อื่นที่ไม่เกี่ยวข้อง `mom-image-app:test` ซึ่งไม่ได้สร้างใน session นี้ | E109 |
| 16 | TIME_UNKNOWN | ผู้สอบขอเพิ่ม "AI workflow สร้างร่าง Customer Update จากข้อมูลในฐานข้อมูล" | ผู้สอบสั่ง | AI เปิดอ่าน skill อ้างอิง Claude API ก่อนเขียนโค้ด (ตาม trigger คำว่า Claude/Anthropic) | E113 |
| 17 | mtime 11:55:17 | สร้าง `app/ai_report.py` (เรียก Claude API แบบ non-streaming, model `claude-opus-4-8`) | AI | — | E013 |
| 18 | mtime 11:56:28 | สร้าง `app/tests/test_ai_report.py` (4 test, mock การเรียก API ทั้งหมด ไม่มีการเรียก API จริง) | AI | pytest ผ่านครบ 24 test (เพิ่มจาก 20) | E011, E103 |
| 19 | TIME_UNKNOWN | แก้ `app/app.py` ให้มีปุ่ม "Generate Customer Update Draft"; ทดสอบผ่าน `AppTest` กรณีไม่มี `ANTHROPIC_API_KEY` → แสดง error สุภาพ ไม่ crash | AI | ยืนยันพฤติกรรม graceful-failure ผ่านการรันจริง | E106 (ส่วนขยาย) |
| 20 | TIME_UNKNOWN | รีสตาร์ท Streamlit server (PID ที่ยังทำงานอยู่ขณะรวบรวมหลักฐาน — E015) | AI | HTTP 200 | E015 |
| 21 | mtime 12:04:33 | สร้างเอกสาร `docs/ddd-bundle/AI_MODEL_SPEC.md` เพื่อปิดช่องว่างเอกสารที่เคยระบุว่า "ไม่เกี่ยวข้อง" (ตอนนี้เกี่ยวข้องแล้วเพราะมี AI model จริง) | AI | — | — |
| 22 | TIME_UNKNOWN (ระหว่างเขียน AI_MODEL_SPEC.md) | ผู้สอบวางคำสั่ง shell export ที่ชี้ไปยัง OpenRouter (พร้อม placeholder key ภาษาไทย "คีย์ของคุณ") โดยไม่มีคำอธิบายเจตนา | ผู้สอบ | AI **ไม่รันคำสั่งดังกล่าว** และถามกลับเพื่อยืนยันเจตนา ผู้สอบตอบว่า "วางผิดที่" | E114 |
| 23 | TIME_UNKNOWN | ผู้สอบขอให้ "set ANTHROPIC_API_KEY ใน .env แล้วลองใช้งาน" | ผู้สอบสั่ง | AI ตรวจสอบว่าไม่มี credential ใด ๆ อยู่ในเครื่อง (ไม่มี env var, ไม่มี `ant` CLI) จึงถามผู้สอบให้ส่ง key มาจริง ผู้สอบตอบว่า "จะวาง key ตอนนี้" — **บทสนทนาจบลงด้วยคำร้องขอรวบรวมหลักฐานก่อนที่จะมีการส่ง key จริงเข้ามา** | E115 |
| 24 | 2026-10-02T11:42:30+07:00 | **Git commit `70a9a52` ("First commit") ถูกสร้างขึ้น** พร้อม remote `origin` ชี้ไปที่ GitHub | ไม่ทราบแน่ชัด — ไม่ปรากฏเป็น tool call ที่มองเห็นได้ในบทสนทนานี้ (ดูหมวด B) | สถานะ local แสดงว่า branch ตรงกับ `origin/master` | E001, E003 |
| 25 | 12:06:44 (เวลาเริ่มรวบรวมหลักฐาน) | ผู้สอบร้องขอให้รวบรวมหลักฐานงานสอบ | ผู้สอบ | เริ่มกระบวนการที่บันทึกในเอกสารนี้ | — |

**หมายเหตุสำคัญเรื่องลำดับเวลา:** จุดที่ 24 (git commit) มีเวลานาฬิกา 11:42:30 ซึ่งอยู่ **ระหว่าง** ลำดับที่ 15 (docker images, ก่อน 11:42) และลำดับที่ 16–23 (AI workflow, มี mtime หลัง 11:55) ตามลำดับเวลานาฬิกาจริง อย่างไรก็ตามลำดับการ "ปรากฏในบทสนทนา" ของเหตุการณ์ 16–23 มาหลังลำดับ 15 เช่นกัน — จึงสอดคล้องกันว่า commit เกิดขึ้น ณ จุดใดจุดหนึ่งระหว่างการทำงานในบทสนทนา ไม่ใช่ก่อนเริ่มหรือหลังจบทั้งหมด **ไม่สามารถระบุได้แน่ชัดว่า commit นี้เกิดขึ้นจาก terminal คำสั่งใดหรือในขั้นตอนใดของบทสนทนาอย่างแม่นยำ เนื่องจากไม่ปรากฏเป็น tool call ที่มองเห็นได้**

---

## D. คำสั่งและเครื่องมือที่ใช้ระหว่างสอบ

**หมายเหตุ:** ตารางนี้เป็น**การสรุปแบบย่อ** ไม่ใช่รายการคำสั่งทุกคำสั่งที่เกิดขึ้นในบทสนทนาทั้งหมด (มีคำสั่ง Bash/Read/Write/Edit จำนวนมากตลอด session) โดยเลือกเฉพาะคำสั่งที่มีนัยสำคัญต่อการประเมินหลักฐาน คำสั่งที่ปกปิด secrets แล้วหากมี (ไม่พบ secrets ในคำสั่งที่บันทึกไว้)

### D.1 คำสั่งที่มีหลักฐานว่า execute แล้ว (ระหว่างบทสนทนา)

| ลำดับ | คำสั่ง/tool ที่พบ | จุดประสงค์ที่มีหลักฐาน | ผล/exit code ที่พบ | ช่วงเวลา | Evidence ID |
|---|---|---|---|---|---|
| 1 | `pytest -q` / `pytest -v app/tests` (หลายครั้งตลอด session) | ตรวจสอบชุดทดสอบ | "15 passed" → "20 passed" → "24 passed" ตามลำดับการเพิ่มฟีเจอร์ | TIME_UNKNOWN (หลายจุด) | E101, E102, E103 |
| 2 | `python3 -c "..."` เรียก `validate.validate_csv` + `db.load_snapshot` กับไฟล์ CSV จริง | ยืนยันว่า CSV จริง 12,022 แถวผ่าน validation และโหลดเข้า DuckDB สำเร็จ | `accepted: True`, `total: 12022`, `completed: 5461`, `overdue: 3650` | TIME_UNKNOWN | E104 |
| 3 | `python3 -c "..."` query `duckdb_constraints()` บนไฟล์ `.duckdb` จริง | ยืนยัน schema จริงของตารางมี PRIMARY KEY | พบ `PRIMARY KEY` บน `[request_id]` และ `NOT NULL` ทุกคอลัมน์ | TIME_UNKNOWN | E105 |
| 4 | `streamlit run app/app.py --server.port 8765` (nohup, background) หลายครั้ง | รันแอปจริงเพื่อตรวจสอบ | `HTTP 200` จาก `curl` ทุกครั้งที่ทดสอบ | 10:50–12:06 (process ยังทำงานอยู่ขณะรวบรวมหลักฐาน) | E102, E015 |
| 5 | `streamlit.testing.v1.AppTest` (เขียนเป็น python script เรียกผ่าน Bash) | จำลองการใช้งานจริงผ่าน widget (อัปโหลดไฟล์, filter, อัปโหลดไฟล์เสีย) | ยืนยันค่าตรงกับที่คาดไว้ทุกกรณี รวมถึงกรณี error-path | TIME_UNKNOWN | E106 |
| 6 | `docker build -t customer-request-dashboard .` | สร้าง Docker image | สำเร็จ ("DONE 39.4s") หลังเปิด Docker Desktop ก่อน (เดิมไม่ได้เปิดอยู่) | TIME_UNKNOWN | E107 |
| 7 | `docker run -d ... && curl ... && docker rm -f ...` | ทดสอบรัน container จริง | `HTTP 200`, log ยืนยัน Uvicorn/Streamlit บูตสำเร็จ, ลบ container ทดสอบทิ้งหลังตรวจเสร็จ | UTC 04:29 (≈11:29 +07) | E108 |
| 8 | `docker images` | แสดงรายการ image | พบ `customer-request-dashboard:latest` และ image อื่นที่ไม่เกี่ยวข้อง | TIME_UNKNOWN | E109 |
| 9 | Skill `claude-api` (อ้างอิงเอกสารก่อนเขียนโค้ดเรียก Claude API) | ตรวจสอบ model ID และรูปแบบ SDK ที่ถูกต้องก่อนเขียน `ai_report.py` | ได้ข้อมูล model ID `claude-opus-4-8` และรูปแบบ error handling | TIME_UNKNOWN | E113 |
| 10 | Skill `verify` | ตรวจสอบการแก้ไข whitespace/PRIMARY KEY แบบ end-to-end | ผลตรงกับที่ระบุในแถว 5 ข้างต้น | ~11:24–11:29 | E106 |

### D.2 คำสั่งที่เพียงเสนอหรือกล่าวถึง (ไม่มีหลักฐานว่าถูก execute จริงในบทสนทนานี้)

| คำสั่ง/การกระทำที่เสนอ | บริบท | หมายเหตุ |
|---|---|---|
| `docker build` / `docker run` ตามคำแนะนำใน README.md | AI แนะนำให้ผู้สอบรันเองหลังสร้าง Dockerfile ครั้งแรก (ก่อนที่ Docker Desktop จะพร้อมใช้งานใน session) | ไม่ทราบว่าผู้สอบรันเองหรือไม่ในขณะนั้น ภายหลัง AI เป็นผู้รันเองสำเร็จ (ดู D.1 แถว 6–8) |
| `export OPENROUTER_API_KEY=...` และตัวแปรที่เกี่ยวข้อง | ผู้สอบวางคำสั่งนี้ในแชท | **ไม่ถูก execute โดย AI** — AI ปฏิเสธที่จะรันจนกว่าจะยืนยันเจตนา และผู้สอบยืนยันว่า "วางผิดที่" (E114) |
| การเรียก Claude API จริงเพื่อสร้างร่าง Customer Update (`generate_customer_update`) ด้วย API key จริง | ผู้สอบขอให้ "set ANTHROPIC_API_KEY ใน .env แล้วลองใช้งาน" | **ไม่มีหลักฐานว่าถูก execute สำเร็จในบทสนทนานี้** — ไม่มี API key จริงถูกส่งเข้ามาก่อนจบ session (E115) |

### D.3 คำสั่งอ่านอย่างเดียวที่ใช้รวบรวมรายงานหลังสอบ (ทำโดยผู้รวบรวมหลักฐาน ขณะเขียนเอกสารนี้)

`date`, `pwd`, `git rev-parse --show-toplevel`, `git branch --show-current`, `git rev-parse HEAD`, `git log` (รูปแบบต่าง ๆ), `git show --stat HEAD`, `git show HEAD:<path>` (อ่านเนื้อหาไฟล์จาก commit), `git status`, `git branch -vv`, `git for-each-ref`, `git reflog show`, `git remote -v`, `git diff` / `git diff --stat`, `diff` (เทียบไฟล์ซ้ำ), `ls -la`, `find`, `rg` (ค้นคำว่า coolify), `grep -c` (นับจำนวน test function), `cat` (อ่าน `.claude/settings.local.json` และ `.gitignore` ผ่าน `git show`), `ps aux | grep` (ตรวจ process ที่ยังทำงานอยู่) — **ไม่มีการรัน script ของ repo, ไม่มีการรัน test/build/app ใหม่ ไม่มีการ commit/push/fetch ใด ๆ ระหว่างขั้นตอนนี้**

---

## E. การตัดสินใจและการใช้ AI

| การตัดสินใจ | ทางเลือกที่มี | ผลลัพธ์ที่เลือก | เหตุผลที่ปรากฏในหลักฐาน | สถานะ |
|---|---|---|---|---|
| reference_date | "วันนี้ (2026-10-02)" หรือ "ระบุวันที่เอง" | วันนี้ (2026-10-02) | ผู้สอบเลือกผ่าน AskUserQuestion โดยตรง | VERIFIED |
| แหล่งไฟล์ CSV | "จะให้ไฟล์เอง" หรือ "ให้ AI สร้างไฟล์จำลอง" | จะให้ไฟล์เอง | ผู้สอบเลือกผ่าน AskUserQuestion โดยตรง | VERIFIED |
| Tech stack | Python/Streamlit/DuckDB หรือ Node/Next.js/DuckDB หรือระบุเอง | Python (Streamlit) + DuckDB | ผู้สอบเลือกผ่าน AskUserQuestion โดยตรง | VERIFIED |
| นโยบาย case normalization | "คงความเข้มงวด (ไม่ normalize)" หรือ "normalize case อัตโนมัติ" | คงความเข้มงวด (ไม่ normalize) | ผู้สอบเลือกตัวเลือกที่ AI ระบุว่า "แนะนำ" ผ่าน AskUserQuestion หลังอ่านคำอธิบายผลกระทบ | VERIFIED (การเลือก) — **ไม่สามารถสรุปได้ว่าผู้สอบเข้าใจเหตุผลเชิงเทคนิคเบื้องหลังหรือไม่ เป็นเพียงการเลือกตัวเลือกที่ปรากฏ** |
| กฎ "Due Date >= Request Date" | "ระบุว่าใช้ไม่ได้ (ไม่มี column รองรับ)" หรือ "เพิ่ม column ใหม่ในสคีมา" | ระบุว่าใช้ไม่ได้ | ผู้สอบเลือกตัวเลือกที่ AI ระบุว่า "แนะนำ" | VERIFIED (การเลือก) — เช่นเดียวกับข้างต้น |
| ขอบเขต DDD mixing (`CONSTRAINTS.md`/`TASKS.md` ที่พบว่าเป็นของ blueprint `ddd-web-app` ไม่ใช่ `ddd-data-analytics`) | ลบ/เขียนใหม่ หรือ บันทึกเป็นข้อยกเว้นที่ตั้งใจ | บันทึกเป็นข้อยกเว้นที่ตั้งใจใน `00-DDD-SCOPE.md` | เป็นการตัดสินใจของ AI เองในขั้นตอนแก้ไขช่องว่าง (ไม่ปรากฏว่าผู้สอบถูกถามเรื่องนี้โดยตรงก่อนแก้) | REPORTED (เป็นทางเลือกที่ AI เสนอและดำเนินการเอง ไม่มีหลักฐานว่าผู้สอบอนุมัติทางเลือกนี้โดยเฉพาะเจาะจง นอกเหนือจากคำสั่งกว้าง ๆ ว่า "แก้เฉพาะรายการที่ขาด") |
| AI workflow (Customer Update draft) — เลือก model | ไม่ปรากฏว่ามีการเสนอทางเลือก model หลายตัว | `claude-opus-4-8` (ค่าเริ่มต้นตาม skill reference) | AI เลือกตาม default ของเอกสารอ้างอิง ไม่ปรากฏว่าผู้สอบระบุ model เอง | REPORTED |

**Token/Quota การใช้งาน AI:** ไม่มีหลักฐานปรากฏในบทสนทนาหรือไฟล์ repo เกี่ยวกับปริมาณ token หรือ quota ที่ใช้ไป — **UNKNOWN** (ไม่ประมาณการ)

**หลักฐานการตรวจ/ปรับ output ของ AI โดยผู้สอบ:** พบหลักฐานชัดเจนอย่างน้อย 2 จุดที่ผู้สอบต้องเลือกระหว่างทางเลือกที่มีผลต่างกันจริง (นโยบาย case-normalization, กฎ due-date) แทนที่จะปล่อยให้ AI ดำเนินการอัตโนมัติทั้งหมด (ดูตารางข้างต้น) นอกจากนี้ยังมีกรณีที่ผู้สอบสั่งให้ AI "validate" งานตัวเองอย่างละเอียดก่อนให้แก้ไข (ลำดับที่ 9 ในหมวด C) ซึ่งเป็นรูปแบบการทำงานที่มีการตรวจสอบแทรกอยู่ **ไม่มีหลักฐานเพียงพอที่จะสรุปว่าผู้สอบเข้าใจรายละเอียดทางเทคนิคของโค้ดที่ AI เขียนในระดับลึกเพียงใด เนื่องจากไม่ปรากฏบทสนทนาเชิงเทคนิคเชิงลึกจากฝั่งผู้สอบในประเด็นเหล่านี้**

---

## F. ปัญหาและสิ่งที่ติด

| ปัญหา | อาการ/error ที่พบ | วิธีที่ลอง | ผลที่ยืนยันได้ | ยังไม่ทราบ/ยังค้าง | Evidence ID |
|---|---|---|---|---|---|
| Git repo ของโปรเจกต์มี root ผิดที่ (home directory) และไม่มี commit เลย | `fatal: your current branch 'master' does not have any commits yet` | AI แจ้งเตือนผู้สอบ แนะนำให้แยก repo ใหม่ | สถานะปัจจุบันพบว่ามี repo ใหม่ถูกต้องแล้ว (root ที่ `Customer-Request`, มี commit, มี remote) | **ไม่ทราบว่าแก้ไขด้วยคำสั่งใด/ขั้นตอนใด เนื่องจากไม่ปรากฏเป็น tool call ที่มองเห็นได้** | E010, E001 |
| Docker Desktop ไม่ได้เปิดอยู่เมื่อถูกขอให้ `docker build` | `failed to connect to the docker API ... dial unix ...docker.sock: connect: no such file or directory` | AI สั่งเปิด Docker Desktop (`open -a Docker`) แล้ว poll จนกว่า daemon พร้อม | แก้ไขสำเร็จ, build ผ่าน | — | E107 |
| สคริปต์ตรวจสอบ (`AppTest`) เขียนผิดรูปแบบ (`at.selectbox(key=None)[0]` ทำให้เกิด `TypeError`) | `TypeError: 'Selectbox' object is not subscriptable` | AI แก้ไขรูปแบบการเรียกและรันใหม่ทันทีในขั้นตอนเดียวกัน | แก้ไขสำเร็จ รันผ่าน | — | E106 |
| ข้อความเริ่มต้นของผู้สอบกำกวม ("Analyze this repo / run / ทำยังไ") | ไม่สามารถตีความเจตนาได้ชัดเจน | AI ถามคำถามชี้แจง | ผู้สอบชี้แจงเจตนาแล้ว | — | — |
| DDD blueprint ผสมกัน (`CONSTRAINTS.md`/`TASKS.md` ของ `ddd-web-app` ปนอยู่ในชุดเอกสาร `ddd-data-analytics`) | พบระหว่างการตรวจสอบ (validation) | บันทึกเป็นข้อยกเว้นที่ตั้งใจในเอกสาร แทนที่จะลบ/สร้างใหม่ | เอกสารถูกปรับปรุงแล้ว | **ยังไม่มีหลักฐานว่าผู้สอบอนุมัติแนวทางนี้โดยเฉพาะเจาะจง** (ดูหมวด E) | E111, E112 |
| กฎ validation "Due Date >= Request Date" ไม่สามารถทำได้ | ไม่มีคอลัมน์ `request_date` ในสคีมาต้นฉบับ | ผู้สอบเลือกให้ระบุว่า "ใช้ไม่ได้" แทนการเพิ่มคอลัมน์ใหม่ | บันทึกเป็นข้อจำกัดที่ทราบในเอกสาร | **ยังเป็นข้อจำกัดที่ค้างอยู่ ไม่ใช่สิ่งที่ "แก้แล้ว"** | E112 |
| ข้อความหนึ่งของโจทย์ระบุ "Toyota customer cybersecurity service requests" แต่ไม่พบคำว่า "Toyota" ที่ใดใน repo หรือข้อมูลเลย | พบความไม่สอดคล้องระหว่างโจทย์ที่ระบุกับเนื้อหาจริงของ repo | AI แจ้งให้ผู้สอบทราบ | **ไม่ปรากฏว่าผู้สอบตอบกลับประเด็นนี้ในบทสนทนาที่เหลือ** | **ยังค้างอยู่ ไม่มีคำตอบ/คำชี้แจง** | — |
| ไฟล์ซ้ำที่ไม่ทราบที่มา (`app/validate 2.py`, `output/customer_requests 2.duckdb`) | พบระหว่างการรวบรวมหลักฐานครั้งนี้ | ไม่มีการแก้ไข/ลบ (ตามข้อกำหนดห้ามแก้ไข) | — | **ไม่ทราบที่มา ไม่ทราบว่ามีผลกระทบต่อการทำงานจริงหรือไม่** | E008, E009 |
| AI workflow (Customer Update draft) ยังไม่เคยถูกเรียกใช้งานจริงด้วย API key จริง | ไม่มี `ANTHROPIC_API_KEY` ในเครื่อง ไม่มี credential ใด ๆ | AI ขอให้ผู้สอบส่ง key จริงมา | ผู้สอบตอบว่าจะส่ง key แต่บทสนทนาจบก่อนที่จะส่งจริง | **ค้างอยู่ — ไม่มีหลักฐานว่าฟีเจอร์นี้เคยทำงานได้จริงกับ API จริง มีเพียงผลทดสอบแบบ mock** | E115, E103 |

---

## G. งานที่ส่งมอบ

### ฟังก์ชันหลักที่พบในโค้ด (Implementation — พบจริงในไฟล์)

- เส้นทางข้อมูล: อัปโหลด CSV → validate (`app/validate.py`) → โหลดเข้า DuckDB แบบ snapshot เต็ม พร้อม PRIMARY KEY บน `request_id` (`app/db.py`) → คำนวณ metric ผ่าน SQL (`app/metrics.py`) → แสดงผลบน Streamlit (`app/app.py`): KPI card (Total/Completed/Overdue), กราฟ/ตาราง breakdown ตาม service type, ตารางรายการ overdue พร้อม filter ตาม service type และ owner
- เอกสาร DDD ครบ 19 ไฟล์ตาม blueprint `ddd-data-analytics` (รวมไฟล์ที่เพิ่มภายหลัง: `DATA_GOVERNANCE.md`, `DATA_CONTRACT.md`, `REPORT_SPEC.md`, `LINEAGE.md`, `ANALYTICS_CHANGELOG.md`, `AI_MODEL_SPEC.md`)
- การตั้งค่า persistence: ไฟล์ DuckDB แบบไฟล์เดี่ยว (`output/customer_requests.duckdb`), ตั้งค่า path ผ่าน environment variable (`APP_DB_PATH`), แยก `.env.example` ไว้เป็นแม่แบบ
- Dockerfile, `.dockerignore`, และ `docker-compose.yml` (ไฟล์หลังนี้ไม่ได้ถูกสร้างผ่าน tool call ที่ปรากฏในบทสนทนานี้ — ดูหมวด B)
- ฟีเจอร์เสริม: ปุ่มสร้างร่าง Customer Update ด้วย Claude API (`app/ai_report.py`)

### แยก "พบ implementation" จาก "มีหลักฐานใช้งานสำเร็จ"

| ส่วนประกอบ | พบ implementation | มีหลักฐานใช้งานสำเร็จจริง (ภายใน session นี้) |
|---|---|---|
| CSV validation + โหลด DuckDB | ใช่ | ใช่ — ทดสอบกับไฟล์จริง 12,022 แถว ผ่านทั้งแบบเรียกฟังก์ชันตรงและผ่าน UI จริง (E104, E106) |
| Dashboard (KPI/breakdown/filter) | ใช่ | ใช่ — ยืนยันผ่าน `AppTest` จริง รวมถึง probe กรณี filter และกรณีอัปโหลดไฟล์เสีย (E106) |
| DB-level PRIMARY KEY | ใช่ | ใช่ — ยืนยันด้วย query `duckdb_constraints()` จริง (E105) |
| Docker image/container | ใช่ | ใช่ — build และ run จริงสำเร็จ (E107, E108) |
| `docker-compose.yml` | ใช่ (พบในไฟล์ที่ commit แล้ว) | **ไม่มีหลักฐาน** ว่าเคยถูกรันด้วย `docker compose up` ใน session นี้ |
| AI Customer Update draft | ใช่ (โค้ดสมบูรณ์, มี error handling) | **ไม่มี** — ทดสอบด้วย mock เท่านั้น (E103), กรณีไม่มี key ยืนยันว่า error สุภาพไม่ crash (E106 ส่วนขยาย), **แต่ไม่เคยเรียก Claude API จริงสำเร็จในบทสนทนานี้** |

### ข้อจำกัดที่พบ (ไม่ได้ทดลองใหม่ ตามข้อห้าม)

- ไม่ทราบว่า `docker-compose.yml` ใช้งานได้จริงหรือไม่ เนื่องจากไม่เคยถูกรัน
- ไม่ทราบว่า DuckDB แบบไฟล์เดี่ยวรองรับผู้ใช้หลายคนพร้อมกันหรือไม่ (ไม่มีการทดสอบ concurrency)
- ไม่มีการทดสอบ deploy บน environment อื่นนอกเหนือจากเครื่อง local ของผู้สอบ

---

## H. หลักฐาน Test / Validation

### กรณีทดสอบที่พบในโค้ด (static, นับจากไฟล์จริงขณะรวบรวมหลักฐาน — E011)

| ไฟล์ | จำนวน test function | สถานะใน Git |
|---|---|---|
| `app/tests/test_validate.py` | 10 | committed (ตรงกับ working tree ปัจจุบัน) |
| `app/tests/test_metrics.py` | 10 | committed (ตรงกับ working tree ปัจจุบัน) |
| `app/tests/test_ai_report.py` | 4 | **untracked** (ยังไม่ commit) |
| **รวม** | **24** | — |

### ผลรันจริงที่พบในบทสนทนา (dynamic — ปรากฏใน session นี้เท่านั้น ไม่มีไฟล์ log แยกต่างหากบนดิสก์)

| รอบ | ผลลัพธ์ที่รายงานในบทสนทนา | จำนวน test ที่สอดคล้องกับไฟล์ ณ ขณะนั้น | Evidence ID |
|---|---|---|---|
| หลังสร้างแอปครั้งแรก | "14 passed" → ภายหลัง "15 passed" (เพิ่ม owner filter test) | สอดคล้องกับจำนวน test ในช่วงก่อนรอบแก้ไข validation | E101 |
| หลังแก้ whitespace + PK constraint | "20 passed" | ตรงกับ 10+10 = 20 ของไฟล์ที่ commit แล้ว | E102 |
| หลังเพิ่ม AI workflow | "24 passed" | ตรงกับ 10+10+4 = 24 (รวมไฟล์ที่ยังไม่ commit) | E103 |

**ข้อสังเกต:** ผลรันทั้งหมดข้างต้นเป็น **ผลที่ปรากฏในข้อความของบทสนทนา (tool call output)** ไม่ใช่ไฟล์ log แยกต่างหากที่หลงเหลืออยู่บนดิสก์ ขณะรวบรวมหลักฐานนี้ **ไม่ได้มีการรัน `pytest` ใหม่เพื่อยืนยันซ้ำ** ตามข้อห้ามไม่ให้รัน validation ใหม่ จึงไม่สามารถยืนยันว่า ณ ขณะนี้ (หลังสอบ) test ทั้ง 24 รายการยังคงผ่านอยู่จริงหรือไม่ — สถานะคือ **VERIFIED เฉพาะ ณ เวลาที่รันในบทสนทนา (TIME_UNKNOWN ตำแหน่งแน่นอน แต่ยืนยันว่าเกิดก่อน commit `70a9a52` สำหรับรอบ 20 test และหลัง commit สำหรับการเพิ่ม 4 test ของ AI workflow)**

### หลักฐานการตรวจสอบระดับ UI จริง (ไม่ใช่แค่ unit test)

พบการตรวจสอบผ่าน `streamlit.testing.v1.AppTest` ซึ่งรันสคริปต์แอปจริงผ่าน engine ของ Streamlit (ไม่ใช่การเรียกฟังก์ชันภายในตรง ๆ) ครอบคลุม: อัปโหลดไฟล์ CSV จริงผ่าน widget, ตรวจค่า KPI ที่ render จริง, ทดสอบ interaction ของ filter, ทดสอบ probe กรณีอัปโหลดไฟล์ผิดรูปแบบขณะมี snapshot เดิมอยู่แล้ว (ยืนยันว่า snapshot เดิมไม่ถูกเขียนทับ) — E106 **นี่คือหลักฐานการทดสอบที่มีความน่าเชื่อถือสูงสุดในเอกสารนี้ เนื่องจากจำลองการใช้งานจริงของผู้ใช้ปลายทางผ่าน widget จริง ไม่ใช่เพียงการเรียก function โดยตรง**

---

## I. หลักฐาน Repo และ Coolify

| รายการ | ค่าที่พบ | สถานะ |
|---|---|---|
| Repo URL | `git@github.com:Nannaphat40/Customer-Request.git` | VERIFIED (จาก `git remote -v` — E006) |
| Commit SHA (HEAD ปัจจุบัน) | `70a9a52c3162b15ba391213de772fa0f5cb60bf8` | VERIFIED (E001) |
| หลักฐานการ push | local remote-tracking ref `refs/remotes/origin/master` ชี้ไปที่ commit เดียวกับ local `master` | VERIFIED **เฉพาะในระดับ local record เท่านั้น** — **ไม่ได้ทำการ fetch เพื่อยืนยันว่า GitHub มี commit นี้จริง ณ ขณะนี้** ตามข้อกำหนดห้ามเรียกบริการภายนอกเพิ่ม จึงไม่สามารถยืนยัน "push สำเร็จจริงบน GitHub" ได้ 100% — มีเพียงหลักฐานทางอ้อมว่า local repo เคยซิงก์กับ remote นี้มาก่อน |
| เวลา push จริง เทียบกับกำหนดเวลาสอบ | ไม่ทราบ | UNKNOWN (ไม่ทราบทั้งเวลา push จริงบน GitHub และเวลากำหนดส่งสอบ) |
| Deployment ID/URL (เช่น Coolify) | ไม่พบเลย | UNKNOWN / ไม่พบหลักฐาน — ค้นหาคำว่า "coolify" ทั่ว repo ไม่พบ (E016), ไม่พบไฟล์ CI/CD หรือ deployment config ใด ๆ (E017), ไม่มีการกล่าวถึง Coolify ในบทสนทนาทั้งหมดที่เข้าถึงได้ |
| Commit ที่ deploy | ไม่สามารถระบุได้ เนื่องจากไม่พบหลักฐานการ deploy ใด ๆ | UNKNOWN |
| ผลเปิดใช้งานจริงบน production/hosting | ไม่พบ — มีเพียง Streamlit dev server รันบนเครื่อง local ของผู้สอบเอง (พอร์ต 8765) ซึ่ง**ไม่ใช่การ deploy สู่สภาพแวดล้อมสาธารณะ** | VERIFIED (ว่าเป็น local process เท่านั้น — E015) |

**สรุปสำคัญ:** local commit และ remote-tracking branch เพียงอย่างเดียว **ไม่ยืนยันว่า push ทันเวลา** และ**ไม่พบ URL แอปที่ deploy บน hosting ใด ๆ เลยตลอดบทสนทนานี้** — ไม่มีหลักฐาน Coolify หรือ deployment หลักฐานใด ๆ ทั้งสิ้น

---

## J. หลักฐาน AI workflow โบนัส

### Pipeline ที่พบในโค้ด (`app/ai_report.py`, `app/app.py`)

| ขั้นตอน | รายละเอียดที่พบในโค้ด |
|---|---|
| Trigger | ปุ่ม `st.button("Generate Customer Update Draft")` ใน `app/app.py` |
| Input จาก DB | ค่าที่คำนวณแล้วจาก `metrics.get_total_requests/get_completed_requests/get_overdue_requests` (ตาม filter ปัจจุบัน), ตาราง breakdown จาก `metrics.get_breakdown_by_type`, รายการ overdue จาก `metrics.get_overdue_detail` — **โมเดลไม่ได้เข้าถึงฐานข้อมูลโดยตรง** ได้รับเฉพาะค่าที่คำนวณไว้แล้วเป็น text ในพรอมป์ |
| AI call | `anthropic.Anthropic().messages.create(model="claude-opus-4-8", max_tokens=2048, messages=[...])` แบบ non-streaming เรียกครั้งเดียว ไม่มี tool use |
| การตรวจ output | ตรวจ `response.stop_reason == "refusal"` และตรวจว่ามี text block ไม่ว่างเปล่า ก่อนส่งคืนผลลัพธ์ |
| การบันทึก/แสดงผล | แสดงใน `st.text_area` พร้อมข้อความกำกับชัดเจนว่าเป็นฉบับร่างที่ต้องตรวจสอบก่อนส่งจริง — **ไม่มีเส้นทางส่งอัตโนมัติไปยังลูกค้า** |
| Error handling | ครอบคลุม: ไม่มี API key, API key ผิด (`AuthenticationError`), rate limit, connection error, API status error ทั่วไป — ทุกกรณีแปลงเป็น `AIReportError` พร้อมข้อความอธิบายที่เข้าใจง่าย |
| Logs | ไม่พบไฟล์ log เฉพาะของฟีเจอร์นี้บนดิสก์ |

### แยก runtime AI workflow ออกจากการใช้ Claude Code ช่วยเขียนโค้ด

ฟีเจอร์นี้ **เป็น AI workflow ที่ทำงานตอน runtime ของแอป (เรียก Claude API เมื่อผู้ใช้กดปุ่ม)** แยกต่างหากจากการที่ Claude Code ถูกใช้เป็นเครื่องมือเขียนโค้ดทั้งโปรเจกต์ (ซึ่งเป็นอีกเรื่องหนึ่ง อยู่ในหมวด A/D)

### ข้อจำกัดสำคัญที่ต้องระบุชัดเจน

**ไม่มีหลักฐานว่าฟีเจอร์นี้เคยถูกเรียกใช้งานจริงสำเร็จด้วย Claude API จริงเลยตลอด session นี้** การทดสอบที่มีอยู่ทั้งหมดเป็น:
1. Unit test แบบ **mock** การเรียก API ทั้ง 4 กรณี (E103) — ไม่มีการเชื่อมต่อ network จริง
2. การทดสอบผ่าน `AppTest` ยืนยันเพียงว่า **กรณีไม่มี API key** แอปแสดง error อย่างสุภาพโดยไม่ crash (ส่วนขยายของ E106)

เมื่อผู้สอบขอให้ตั้งค่า `ANTHROPIC_API_KEY` จริงและทดลองใช้งาน (ลำดับ 23 ในหมวด C) **บทสนทนาจบลงก่อนที่จะมีการส่ง key จริงเข้ามา** จึงไม่มีหลักฐานข้อความร่าง (draft text) ที่มาจากการเรียก Claude API จริงเลยแม้แต่ครั้งเดียวในเอกสารนี้

---

## K. ตารางหลักฐานตามเกณฑ์สอบ

| หัวข้อ | หลักฐานที่รองรับ | Evidence ID | สถานะหลักฐาน | สิ่งที่ยังยืนยันไม่ได้ |
|---|---|---|---|---|
| ประโยชน์และฟังก์ชันหลัก | CSV→validate→DuckDB→dashboard ทำงานได้จริงกับข้อมูลจริง 12,022 แถว ยืนยันผ่าน UI จริง | E104, E106 | VERIFIED (ภายใน session นี้) | ยังไม่มีการตรวจยืนยันอิสระนอกเหนือจาก session นี้ (เช่น กรรมการรันเองซ้ำ) |
| การใช้ DDD | เลือก blueprint `ddd-data-analytics`, มีเอกสารครบ 19 ไฟล์ตาม generation_order, มีข้อยกเว้นที่บันทึกไว้ชัดเจน (เอกสาร 2 ไฟล์ปนจาก `ddd-web-app`) | E003, E004, E111, E112 | VERIFIED (โครงสร้างเอกสาร) / REPORTED (เหตุผลเชิงลึกบางจุดมาจาก AI ไม่ใช่ผู้สอบโดยตรง) | ไม่ทราบว่าผู้สอบเป็นผู้เลือก blueprint นี้เองตั้งแต่ต้น หรือมีอยู่ก่อนหน้า session นี้แล้ว |
| ฐานข้อมูลและ persistence | DuckDB ไฟล์เดี่ยว มี PRIMARY KEY จริง (ยืนยันด้วย query), โหลดข้อมูลจริงสำเร็จ | E105, E104 | VERIFIED | ไม่ทดสอบ concurrency/multi-user |
| Test / Validation | 24 test function ในไฟล์ (10+10 committed, 4 untracked), ผลรันจริงในบทสนทนา 15→20→24 passed, มีการทดสอบระดับ UI จริงผ่าน AppTest | E011, E101, E102, E103, E106 | VERIFIED (ณ เวลาที่รันในบทสนทนา) | ไม่ยืนยันว่า ณ ขณะนี้ (หลังสอบ) test ยังผ่านอยู่ทั้งหมด เนื่องจากไม่อนุญาตให้รันซ้ำ; ไม่มี CI อัตโนมัติที่ gate การ merge |
| Push repo และ Coolify deployment | มี remote origin + commit เดียว + local tracking ref ตรงกับ origin/master (ตามความรู้ local) | E001, E002, E006, E007 | VERIFIED (เฉพาะสถานะ local) / **UNKNOWN (Coolify ทั้งหมด)** | ไม่ยืนยันว่า push ถึง GitHub จริงหรือทันเวลา (ไม่ได้ fetch); **ไม่พบหลักฐาน Coolify หรือ deployment ใด ๆ เลย** |
| การใช้งานและส่งมอบ | แอปรันได้จริง ทั้งแบบ local Streamlit และ Docker container | E102, E106, E107, E108 | VERIFIED | ไม่มีหลักฐานการใช้งานบน environment ที่ไม่ใช่เครื่อง local ของผู้สอบ/ผู้รวบรวมหลักฐาน |
| AI workflow โบนัส | พบ implementation สมบูรณ์ มี error handling ครบ มี unit test (mock) | E013, E103, E106 | VERIFIED (เฉพาะ code + mock test) | **ไม่มีหลักฐานการเรียก Claude API จริงสำเร็จแม้แต่ครั้งเดียว** — ยังไม่เคยพิสูจน์ว่าทำงานได้จริงกับ API จริง |

### เงื่อนไขบังคับ (แยกตามที่กำหนด)

| เงื่อนไข | ผล |
|---|---|
| ฟังก์ชันหลักใช้ได้ | VERIFIED — ยืนยันผ่านการทดสอบจริงภายใน session นี้ (E104, E106) |
| ใช้ DB จริง | VERIFIED — DuckDB พร้อม PRIMARY KEY ยืนยันด้วย query จริง (E105) |
| มี Test/Validation ผ่าน | VERIFIED (ณ เวลาที่รันในบทสนทนา, ไม่ใช่ CI อัตโนมัติ) — ดูหมวด H |
| Push ทันเวลา | UNKNOWN — ไม่ทราบเวลากำหนดส่งสอบ และไม่สามารถยืนยันสถานะ GitHub จริงได้ (ไม่ได้ fetch) |
| Deploy เปิดใช้ทันเวลา | UNKNOWN — ไม่พบหลักฐาน Coolify หรือ deployment ใด ๆ เลยตลอด session |

---

## L. Evidence Index

| ID | ประเภทแหล่งข้อมูล / ตำแหน่ง | Excerpt (ปกปิด secrets แล้ว) | ช่วงเวลา | ข้อเท็จจริงที่รองรับ |
|---|---|---|---|---|
| E001 | Git log — `git log --format=...` ที่ repo `/Users/carelory/Desktop/Customer-Request` | `commit 70a9a52c3162b15ba391213de772fa0f5cb60bf8` / `Author: Nannaphat Phongphaew <nannaphat.p@ragnar.co.th>` / `AuthorDate: 2026-10-02T11:42:30+07:00` / `First commit` | TIME_UNKNOWN (เวลา commit คือ 11:42:30 แต่ไม่ทราบว่าตรงกับช่วงใดของเวลาสอบจริง) | ยืนยันตัวตนผู้สอบ, เวลา commit, ข้อความ commit |
| E002 | Git command — `git rev-parse --show-toplevel`, `git status` ขณะรวบรวมหลักฐาน (12:06:44+) | `/Users/carelory/Desktop/Customer-Request` / `On branch master, up to date with 'origin/master'` | AFTER_EXAM (ขณะรวบรวมหลักฐาน) | ยืนยัน repo root และสถานะ working tree ขณะรวบรวมหลักฐาน |
| E003 | Git command — `git show --stat HEAD` | รายการไฟล์ 43 ไฟล์ "43 files changed, 10770 insertions(+)" | TIME_UNKNOWN | ยืนยันเนื้อหาที่อยู่ใน commit เดียวที่มีอยู่ |
| E004 | ไฟล์ `docs/ddd-bundle/00-DDD-SCOPE.md` (อ่านตรงจาก working tree, ตรงกับที่ commit) | "Selected blueprint: `ddd-data-analytics-v2.4.0`" | TIME_UNKNOWN | ยืนยันการเลือก DDD blueprint |
| E005 | ไฟล์ `.claude/settings.local.json` | `{"permissions": {"allow": ["Bash(python3 -c ' *)"]}}` | TIME_UNKNOWN | ยืนยันการใช้ Claude Code CLI ใน working directory นี้ |
| E006 | Git command — `git remote -v` | `origin git@github.com:Nannaphat40/Customer-Request.git (fetch/push)` | AFTER_EXAM (ตรวจขณะรวบรวมหลักฐาน) | ยืนยัน remote URL ที่ตั้งค่าไว้ใน local repo |
| E007 | Git command — `git branch -vv`, `git for-each-ref refs/remotes` | `* master 70a9a52 [origin/master] First commit` | AFTER_EXAM | ยืนยันว่า local tracking ref ตรงกับ local HEAD (ไม่ใช่การยืนยันสถานะ GitHub จริง) |
| E008 | คำสั่ง `diff app/validate.py "app/validate 2.py"` | พบส่วนต่าง 2 จุด (whitespace normalization, comment นโยบาย case) ที่มีใน `validate.py` แต่ไม่มีใน `validate 2.py` | AFTER_EXAM | ยืนยันว่า `validate 2.py` เป็นเวอร์ชันเก่ากว่า |
| E009 | คำสั่ง `ls -la output/` | `customer_requests 2.duckdb` 1,060,864 bytes mtime 10:50 / `customer_requests.duckdb` 2,895,872 bytes mtime 11:25 | AFTER_EXAM (ตรวจขณะรวบรวมหลักฐาน; mtime เป็นข้อมูลประกอบเท่านั้น ไม่ใช่หลักฐานชี้ขาดเรื่องเวลา) | ยืนยันการมีอยู่ของไฟล์ซ้ำและขนาด/เวลาที่ต่างกัน |
| E010 | บทสนทนาต้น session (ก่อน restructuring) | `fatal: your current branch 'master' does not have any commits yet`, repo root = `/Users/carelory` | TIME_UNKNOWN (ต้น session) | ยืนยันสภาพ Git ที่ผิดปกติในช่วงต้นของบทสนทนา |
| E011 | คำสั่ง `grep -c "^def test_" <file>` | `test_validate.py: 10`, `test_metrics.py: 10`, `test_ai_report.py: 4` | AFTER_EXAM | ยืนยันจำนวน test function ที่มีอยู่จริงในไฟล์ขณะรวบรวมหลักฐาน |
| E012 | ไฟล์ `app/db.py` (grep "PRIMARY KEY") | `request_id VARCHAR PRIMARY KEY` | TIME_UNKNOWN (ตรงกับ commit) | ยืนยัน schema มี PRIMARY KEY ในโค้ดจริง |
| E013 | คำสั่ง `git diff -- app/app.py` | diff แสดงการเพิ่ม `import ai_report` และปุ่ม "Generate Customer Update Draft" | AFTER_EXAM (เปรียบเทียบ working tree กับ HEAD) | ยืนยันการเปลี่ยนแปลง `app.py` หลัง commit เพื่อรองรับ AI workflow |
| E014 | คำสั่ง `git diff --stat` | `.env.example \| 4 ++`, `app/app.py \| 48 +++...`, `docs/ddd-bundle/DASHBOARD_SPEC.md \| 4 ++`, `requirements.txt \| 1 +` | AFTER_EXAM | ยืนยันขอบเขตการเปลี่ยนแปลงหลัง commit |
| E015 | คำสั่ง `ps aux \| grep streamlit` | process PID 71616 `streamlit run app/app.py --server.port 8765` เริ่ม 11:59AM ยังทำงานอยู่ขณะรวบรวมหลักฐาน | AFTER_EXAM (ยืนยันว่า process ยังทำงานอยู่ ณ 12:06+) | ยืนยันว่า Streamlit server ที่เริ่มในบทสนทนายังทำงานอยู่จริงบนเครื่อง |
| E016 | คำสั่ง `rg -il "coolify"` ทั่ว repo | ไม่พบผลลัพธ์ | AFTER_EXAM | ยืนยันว่าไม่มีคำว่า Coolify ปรากฏในไฟล์ใด ๆ ของ repo |
| E017 | คำสั่ง `find ... -iname "*.yml" -o -iname "*.yaml"` | พบเฉพาะ `docker-compose.yml` ไม่พบไฟล์ CI/CD (`.github/workflows/*`) | AFTER_EXAM | ยืนยันว่าไม่มี pipeline อัตโนมัติใด ๆ ใน repo |
| E018 | คำสั่ง `git -C /Users/carelory/Desktop rev-parse --show-toplevel` | `/Users/carelory` | AFTER_EXAM | ยืนยันว่า `/Users/carelory/Desktop` ยังอยู่ภายใต้ repo (ไม่เกี่ยวข้องกับงานสอบ) ที่ root คือ home directory |
| E101 | บทสนทนา — ผล `pytest` ครั้งแรกและหลังเพิ่ม owner filter | "14 passed" → "15 passed" | TIME_UNKNOWN | ยืนยันผลการรัน test รอบแรกของแอป |
| E102 | บทสนทนา — ผล `pytest` หลังแก้ whitespace + PK, และผล `curl` HTTP 200 จาก Streamlit หลายรอบ | "20 passed", "HTTP 200" | TIME_UNKNOWN (ก่อน commit) | ยืนยันผลการรัน test และแอปหลังรอบแก้ไขช่องว่างจาก validation |
| E103 | บทสนทนา — ผล `pytest` หลังเพิ่ม AI workflow | "24 passed" | TIME_UNKNOWN (หลัง commit, ตาม mtime ไฟล์) | ยืนยันผลการรัน test หลังเพิ่มฟีเจอร์ AI |
| E104 | บทสนทนา — ผลเรียก `validate_csv`/`load_snapshot` กับ CSV จริง | `accepted: True, rows: 12022`, `total: 12022, completed: 5461, overdue: 3650` | TIME_UNKNOWN | ยืนยันว่าไฟล์ CSV จริงผ่าน validation และคำนวณ metric ถูกต้อง |
| E105 | บทสนทนา — ผล query `duckdb_constraints()` | ตาราง constraint แสดง `PRIMARY KEY [request_id]`, `NOT NULL` ทุกคอลัมน์ | TIME_UNKNOWN | ยืนยัน schema จริงของฐานข้อมูลมี PRIMARY KEY |
| E106 | บทสนทนา — ผลการรัน `streamlit.testing.v1.AppTest` (หลายรอบ ผ่าน skill `verify` และการทดสอบ AI-button) | ค่า metric ที่ render: `Total Requests: 12022` ฯลฯ, ข้อความ error กรณีไม่มี API key | TIME_UNKNOWN (หลายจุดในบทสนทนา) | ยืนยันพฤติกรรม UI จริงหลายกรณี รวม error-path |
| E107 | บทสนทนา — log `docker build` | `#11 DONE 39.4s`, `naming to docker.io/library/customer-request-dashboard:latest done` | TIME_UNKNOWN | ยืนยันการ build image สำเร็จ |
| E108 | บทสนทนา — log `docker run` + `curl` | `HTTP 200`, `Uvicorn server started on 0.0.0.0:8501` | UTC 04:29 (≈ 11:29 +07) | ยืนยันการรัน container สำเร็จ |
| E109 | บทสนทนา — ผล `docker images` | `customer-request-dashboard:latest 202MB`, `mom-image-app:test ... (ไม่เกี่ยวข้อง)` | TIME_UNKNOWN | ยืนยันการมีอยู่ของ image และชี้แจงว่า image อื่นไม่เกี่ยวข้องกับ session นี้ |
| E110 | (อ้างอิงซ้ำกับ E010) | — | — | — |
| E111 | บทสนทนา — รายงาน "Project Validation Report" ฉบับเต็มที่ AI จัดทำตามคำขอผู้สอบ | หัวข้อ DDD/Agents/Skills/CSV/Business logic/DB/Tests พร้อมสถานะ PASS/PARTIAL/FAIL ของแต่ละหัวข้อ | TIME_UNKNOWN | ยืนยันว่ามีกระบวนการตรวจสอบตนเองอย่างเป็นระบบเกิดขึ้นระหว่าง session |
| E112 | บทสนทนา — AskUserQuestion 2 ข้อ (case-normalization, due-date rule) และคำตอบของผู้สอบ | "Keep strict reject (recommended)", "Mark not-applicable (recommended)" | TIME_UNKNOWN | ยืนยันว่าผู้สอบเป็นผู้ตัดสินใจเลือกทางเลือกเชิงนโยบายเอง |
| E113 | บทสนทนา — การเรียกใช้ skill `claude-api` ก่อนเขียน `ai_report.py` | เนื้อหาระบุ model `claude-opus-4-8`, รูปแบบ `anthropic.Anthropic().messages.create(...)` | TIME_UNKNOWN | ยืนยันว่ามีการอ้างอิงเอกสารทางการก่อนเขียนโค้ดเรียก Claude API |
| E114 | บทสนทนา — ข้อความผู้สอบที่วางคำสั่ง export OpenRouter, และการตอบกลับของ AI/ผู้สอบ | คำสั่ง `export OPENROUTER_API_KEY="คีย์ของคุณ"` ฯลฯ / คำตอบผู้สอบ: "Nothing — I pasted this by mistake" | TIME_UNKNOWN | ยืนยันว่า AI ไม่ execute คำสั่งที่น่าสงสัยโดยไม่ถามก่อน และผู้สอบยืนยันว่าเป็นการวางผิดที่ |
| E115 | บทสนทนา — คำขอ "set ANTHROPIC_API_KEY ใน .env และลองใช้งาน" และผลตรวจสอบ credential | ผลตรวจ: `env ANTHROPIC_API_KEY set: no`, `ant CLI not installed`; AI ถามขอ key จริง ผู้สอบตอบ "I'll paste the key now" | TIME_UNKNOWN (ท้าย session) | ยืนยันว่าไม่มี credential จริงอยู่ในเครื่อง และฟีเจอร์ AI ยังไม่เคยถูกเรียกใช้งานจริงก่อนจบ session |

---

## รายการที่กรรมการควรตรวจเพิ่มเติม (ไม่ใช่การให้คะแนน)

1. ตรวจสอบสถานะจริงบน GitHub (`git@github.com:Nannaphat40/Customer-Request.git`) ว่ามี commit `70a9a52` อยู่จริงหรือไม่ และ push เมื่อใดเทียบกับกำหนดเวลาสอบ — เอกสารนี้ตรวจได้เฉพาะสถานะ local เท่านั้น
2. ยืนยันกับผู้สอบโดยตรงว่าใครเป็นผู้ดำเนินการสร้าง Git repo ใหม่/commit/remote (ไม่ปรากฏเป็น tool call ในบทสนทนานี้)
3. สอบถามผู้สอบเรื่องการ deploy บน Coolify (หรือ hosting ใด ๆ) เนื่องจากไม่พบหลักฐานใด ๆ เลยในบทสนทนาหรือไฟล์ repo
4. ทดสอบฟีเจอร์ AI workflow (Customer Update draft) ด้วย `ANTHROPIC_API_KEY` จริง เนื่องจากไม่เคยมีการเรียก Claude API จริงสำเร็จตลอด session นี้
5. สอบถามผู้สอบเรื่องความไม่สอดคล้องของคำว่า "Toyota" ที่ปรากฏในข้อความโจทย์หนึ่งครั้งแต่ไม่มีหลักฐานเกี่ยวข้องใด ๆ ในระบบ — ประเด็นนี้ไม่เคยได้รับคำชี้แจงจากผู้สอบ
6. สอบถามที่มาของไฟล์ซ้ำ `app/validate 2.py` และ `output/customer_requests 2.duckdb` ว่าเกิดจากกระบวนการใด
7. ยืนยันว่า commit `70a9a52` คือ commit ที่ตั้งใจส่งสอบจริงหรือไม่ (เอกสารนี้ระบุเป็น INFERRED เท่านั้น)
