# Test Plan: OpenAPI Mock Server

## Assignment Requirements

From assignment brief:
- Generate dynamic API responses based on a Swagger/OpenAPI spec
- Test without real backends

This test plan separates requirements into three categories to guide implementation.

---

## 1. CONFIRMED ASSIGNMENT REQUIREMENTS

These are the core behaviors explicitly required by the assignment.

### Core: Load and Parse OpenAPI/Swagger Specification

| ID | Requirement | Scenario | Expected Result |
|----|-------------|----------|-----------------|
| REQ-1.1 | Load OpenAPI spec from file | Provide path to valid OpenAPI/Swagger file | Tool successfully reads the specification |
| REQ-1.2 | Parse valid YAML or JSON | Spec can be in YAML or JSON format | Both formats are successfully parsed |
| REQ-1.3 | Reject invalid spec format | Provide malformed YAML/JSON | Clear error indicating format problem |
| REQ-1.4 | Handle missing file | Provide nonexistent file path | Clear error indicating file not found |

### Core: Generate Dynamic API Responses

| ID | Requirement | Scenario | Expected Result |
|----|-------------|----------|-----------------|
| REQ-2.1 | Generate response for endpoint | Request endpoint defined in spec | Response is generated (based on spec schema) |
| REQ-2.2 | Generate responses dynamically | Endpoint response schema defined in spec | Response conforms to that schema |
| REQ-2.3 | Support basic data types in responses | Schema defines string, number, boolean types | Responses contain appropriate values |
| REQ-2.4 | Support object responses | Schema defines objects/complex types | Responses include nested structures |
| REQ-2.5 | Support array responses | Schema defines arrays | Responses include array data |

### Core: Enable Testing Without Real Backends

| ID | Requirement | Scenario | Expected Result |
|----|-------------|----------|-----------------|
| REQ-3.1 | Serve as mock API | Tool accepts HTTP requests | Requests are answered with mocked responses |
| REQ-3.2 | Handle multiple endpoints | Spec defines multiple endpoints | Each endpoint can be requested and receives responses |

---

## 2. REASONABLE IMPLEMENTATION ASSUMPTIONS

These are inferred as necessary for a working implementation but not explicitly stated in the assignment.

### Assumed: Specification Processing

| ID | Assumption | Rationale |
|----|-----------|-----------|
| ASM-1.1 | Reject empty specification file | Cannot build mock from empty input; graceful failure needed |
| ASM-1.2 | Validate required OpenAPI fields | A spec needs basic structure (version, paths, schemas) to be usable |
| ASM-1.3 | Support OpenAPI 3.0.x and Swagger 2.0 | Common spec formats; reasonable scope |
| ASM-1.4 | Extract path from spec `paths` object | Standard OpenAPI structure for defining endpoints |
| ASM-1.5 | Extract response schema from spec responses | Needed to know what to generate |

### Assumed: Request/Response Handling

| ID | Assumption | Rationale |
|----|-----------|-----------|
| ASM-2.1 | Parse HTTP method from spec (GET, POST, etc.) | Needed to understand what operations are available |
| ASM-2.2 | Parse path parameters from spec (e.g., `{id}`) | Common OpenAPI feature for parameterized endpoints |
| ASM-2.3 | Parse query parameters from spec | Standard API feature |
| ASM-2.4 | Support request body validation | Needed to ensure mock only accepts valid inputs |
| ASM-2.5 | Return appropriate HTTP status codes | Standard HTTP practice (200, 201, 4xx, 5xx) |

### Assumed: Response Generation

| ID | Assumption | Rationale |
|----|-----------|-----------|
| ASM-3.1 | Generate primitive values (string, int, boolean, number) | Schema describes these types |
| ASM-3.2 | Generate objects with properties as defined in schema | Standard for structured responses |
| ASM-3.3 | Generate arrays with elements matching schema | Standard for collection responses |
| ASM-3.4 | Respect enum constraints in schema | Ensures generated data is valid per spec |
| ASM-3.5 | Include required fields in response | Spec marks fields as required for a reason |

### Assumed: Server Implementation

| ID | Assumption | Rationale |
|----|-----------|-----------|
| ASM-4.1 | Implement as HTTP server (CLI with port argument) | Standard pattern for mock servers |
| ASM-4.2 | Server listens on specified port | Allows flexible deployment |
| ASM-4.3 | Match incoming requests to spec endpoints | Core mock server function |
| ASM-4.4 | Return 404 for undefined endpoints | Standard HTTP behavior |

---

## 3. OPTIONAL / FUTURE EDGE CASES

These are not required for initial implementation and can be addressed later.

### Optional: Advanced OpenAPI Features

| ID | Feature | Note |
|----|---------|------|
| OPT-1.1 | Schema `$ref` references | Resolving schema definitions; consider for v2 |
| OPT-1.2 | `allOf` schema composition | Combining multiple schemas; consider for v2 |
| OPT-1.3 | `oneOf` / `anyOf` discriminators | Complex schema unions; future enhancement |
| OPT-1.4 | Request header validation | Beyond basic implementation |
| OPT-1.5 | Cookie handling | Not core to mock server requirement |
| OPT-1.6 | Authentication/authorization simulation | Can be deferred |

### Optional: Server Features

| ID | Feature | Note |
|----|---------|------|
| OPT-2.1 | Graceful shutdown signal handling | Quality-of-life; not core to requirement |
| OPT-2.2 | Detailed request logging | Debugging aid; can be added later |
| OPT-2.3 | Response caching/consistency | Depends on use case |
| OPT-2.4 | Custom response delay simulation | Nice-to-have for testing timeouts |

### Optional: Data Generation Sophistication

| ID | Feature | Note |
|----|---------|------|
| OPT-3.1 | Deeply nested structures (3+ levels) | Works if basic nesting works |
| OPT-3.2 | Faker library for realistic data | Not required; basic generation sufficient |
| OPT-3.3 | Custom example values from spec | Respecting `example` field; nice-to-have |
| OPT-3.4 | Format constraints (email, UUID, date) | Can enhance later |

### Optional: Error Handling Details

| ID | Feature | Note |
|----|---------|------|
| OPT-4.1 | Detailed validation error messages | Basic errors sufficient initially |
| OPT-4.2 | Request body validation errors | Can be simple initially |
| OPT-4.3 | Handling of file permission errors | Can surface as simple error |

---

## FIRST IMPLEMENTATION SLICE: Load and Parse OpenAPI Specification

**Goal:** Establish minimal foundation for parsing specs.

**Confirmed Requirements Covered:**
- REQ-1.1: Load spec from file
- REQ-1.2: Parse YAML and JSON
- REQ-1.3: Reject invalid format
- REQ-1.4: Handle missing file

**Tests to Write:**
1. Load and parse valid YAML OpenAPI spec
2. Load and parse valid JSON OpenAPI spec
3. Reject malformed YAML with clear error
4. Reject malformed JSON with clear error
5. Handle nonexistent file with clear error

**Implementation Scope (tied to assumptions):**
- Reject empty specification file (ASM-1.1)
- Validate required OpenAPI fields exist (ASM-1.2)

**What This Enables:**
- Minimum viable parser for OpenAPI specs
- Establishes project structure and test patterns
- Foundation to build response generation on top

**What This Does NOT Include Yet:**
- HTTP server or request handling
- Response generation or data synthesis
- Endpoint routing or request matching
- Advanced schema features ($ref, allOf, etc.)
- Any OpenAPI version beyond basic structure validation

---

## Notes

- Tests verify observable behavior: can spec be loaded? Does it fail appropriately?
- Tests are independent: each can run in any order
- Confirmed requirements are the minimum viable scope
- Assumptions are educated guesses based on typical mock server needs; can be revisited if assignment clarifies
- Optional features can be prioritized after core requirements work
