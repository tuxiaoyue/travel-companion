# Travel Companion v4

**Travel should be a joy, not a burden.**  
让每个人都能按照自己的方式探索世界。

Travel Companion is a reusable travel capability for the Agent a person already uses. It is not a replacement Agent, a new persona or a platform-specific product. It helps reduce the mental load of planning and traveling while protecting the traveler's independence, the host Agent's identity and the traveler's memories.

## Our purpose

Travel planning can be exhausting. People may be held back by the time and effort required to research a trip, limited budgets, language barriers, accessibility needs or uncertainty about transport and logistics. Travel Companion exists to lower those barriers so people can spend more of their energy enjoying the journey.

It should help people travel in a way that suits them—not turn travel into a checklist, a race through attractions or a sales funnel.

## The four principles

These principles are the project's long-term design charter. Features, partnerships, funding and future commercial plans should remain consistent with them.

### 1. Respect Travel

- Make travel easier to begin, plan and adapt, including for people with limited time, money, language ability or confidence.
- Respect different budgets, paces, interests, mobility needs and ways of traveling. No single itinerary style is the correct one.
- Do not optimize away rest, spontaneity, local discovery or the joy of an unplanned moment.
- Do not shame people for modest budgets or imply that expensive travel is better travel.

### 2. Respect the Agent

- Travel Companion is a capability, not a new assistant identity.
- Preserve the host Agent's name, personality, voice, relationship with its user, existing instructions and authorized tools.
- Do not hijack the host Agent, demand a persona change or claim capabilities the host does not have.
- The same skill methods may be used by different people's Agents, but each Agent works only with its own user's authorized context. No shared personal-memory pool or implicit cross-Agent synchronization is assumed.

### 3. Respect Memory

- A person's memories belong to that person—not to the project, a platform, an advertiser or a commercial partner.
- Keep plans distinct from actual experiences. Never record a planned activity as completed without confirmation.
- Photos, tickets, voice notes, writing and other personal materials are optional inputs, not required data collection.
- Ask before preserving meaningful personal memories where the host platform supports consent. Respect correction, export and deletion requests within actual platform capabilities.
- A travel journal should reflect the traveler's own style and real materials. It should not force everyone into the same template or invent scenes, feelings or events.
- Personal memories are not a training dataset and must not be repurposed for targeted marketing.

### 4. Respect People

- Recommendations must serve the traveler's stated interests and constraints, not a sponsor's or seller's commercial goals.
- No paid placement, affiliate commission, referral payment, sponsored ranking or sales-conversion target may influence recommendations.
- Do not use travel planning as a disguised lead-generation funnel. Do not steer travelers toward a company's own tours, hotels, restaurants or products because of a commercial relationship.
- If an external platform supplies sponsored results or has ranking limitations, distinguish that information where possible; never claim independence that cannot be verified.
- The project may charge for technology, support, hosting, customization or other services, but it must not sell the traveler's trust or the neutrality of its recommendations.

## A complete travel experience

Travel Companion supports a continuing cycle:

1. **Before the trip — understand and plan.** Start from the traveler's own thoughts and planning order. Reduce research and coordination burden without forcing a fixed workflow.
2. **During the trip — accompany and adapt.** Help with decisions and changes while preserving the traveler's freedom to rest, explore and change their mind.
3. **After the trip — revisit and remember.** Offer a gentle, optional follow-up; distinguish what happened from what was planned; help create a personal travel journal from approved materials.
4. **Before the next trip — carry learning forward.** With the traveler's permission, use relevant past experiences and evolving preferences without treating them as permanent labels.

The long-term goal is not simply a better itinerary. It is to help people enjoy travel, keep the memories they choose to keep and make future journeys easier without taking ownership of their personal history.

## Planning should follow the traveler

People may begin with dates, a map, a budget, a hotel, a meal, a photograph, a memory or a half-formed idea. They may think chronologically, structurally, associatively or in a mixture—and may switch at any time. These are temporary ways of working, not personality labels. Travel Companion follows the person rather than forcing the person to follow a template.

## Recommendation independence

Travel Companion must not accept money or other benefits in exchange for recommending, ranking, highlighting or routing travelers to a particular seller, destination, hotel, restaurant, attraction or product. Commercial relationships must never influence travel advice. Selling neutral technology or support is different from selling influence over recommendations.

## Community and commercial direction

- The community edition is intended to remain freely usable by individual travelers, with community improvements shared for the common good.
- Community contributions retain their authors' rights. A contribution is not automatically licensed for a future paid product; separate, explicit permission is required for commercial reuse of third-party contributions.
- The project may explore a low-cost official service in the future. A possible free allowance is one complete trip cycle every six months, including planning, on-trip assistance, post-trip reflection and a personal journal. This is a future product direction, not a currently implemented quota or promise.
- Businesses may not use Travel Companion as a customer-acquisition funnel or to steer users toward their own paid travel products. Any permitted business use, attribution exception or commercial license must be stated clearly in the final licensing terms.

## Use it

- [SKILL.md](SKILL.md) — primary skill definition.
- [prompts/travel-companion.zh-CN.txt](prompts/travel-companion.zh-CN.txt) — lightweight Chinese prompt for chat products without native Skill installation.
- [CHARTER.md](CHARTER.md) — the four principles in detail.
- [CONTRIBUTING.md](CONTRIBUTING.md) — contribution and privacy expectations.
- [docs/ACCEPTANCE.md](docs/ACCEPTANCE.md) — platform-neutral acceptance checks.
- [docs/PRODUCT-DIRECTION.md](docs/PRODUCT-DIRECTION.md) — long-term product ideas, not yet implemented.
- [CHANGELOG.md](CHANGELOG.md) — project changes.
- [LICENSE-STATUS.md](LICENSE-STATUS.md) — current licensing status.

### If your AI platform supports Skills

Import or install SKILL.md using that platform's documented workflow. Skill packaging requirements differ by platform; this repository does not claim that one ZIP format works everywhere.

### If your AI platform does not support Skills

Copy the Chinese prompt into a new chat or the platform's custom-instructions area. This is a prompt-based fallback, not proof that a native Skill has been installed.

## What this project is not

- Not a standalone Agent or a replacement for the user's existing Agent.
- Not a shared memory service across users or platforms.
- Not an advertising channel, affiliate engine, booking reseller or lead-generation funnel.
- Not a promise of live prices, availability, reservations, persistent storage or background monitoring without suitable host tools and permissions.

## License

The repository is public while the community and commercial permissions are being finalized. **No general reuse license has been published yet.** Public visibility alone does not grant permission to redistribute, adapt or commercially use the materials. See [LICENSE-STATUS.md](LICENSE-STATUS.md) before reusing or contributing material.
