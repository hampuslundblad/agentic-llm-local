import { describe, expect, it } from "vitest";
import { cn } from "./cn";

describe("cn", () => {
    it("returns a single class", () => {
        expect(cn("foo")).toBe("foo");
    });

    it("merges multiple classes", () => {
        expect(cn("foo", "bar")).toBe("foo bar");
    });

});